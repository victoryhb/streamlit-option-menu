<template>
    <div class="menu">
        <div class="container-xxl d-flex flex-column flex-shrink-0" :class="{'p-3': !isHorizontal, 'p-h':isHorizontal, 'nav-justified': isHorizontal}" :style="styleObjectToString(styles['container'])">
            <template v-if="menuTitle">
                <a href="#" class="menu-title align-items-center mb-md-0 me-md-auto text-decoration-none"
                :style="styleObjectToString(styles['menu-title'])"
                >
                    <i class="icon" :class="menuIcon" :style="styleObjectToString(styles['menu-icon'])"></i>
                    {{menuTitle}}
                </a>
            <hr>
            </template>
            <ul class="nav nav-pills mb-auto" :class="{'flex-column': !isHorizontal, 'nav-justified': isHorizontal}"
            :style="styleObjectToString(styles['nav'])"
            >
                <li class="nav-item" v-for="(option,i) in args.options" :key="option"
                :style="styleObjectToString(styles['nav-item'])"
                >
                    <hr :class="{vr: isHorizontal}" v-if="option === '---'" :style="styleObjectToString(styles['separator'])">
                    <a v-else href="#" class="nav-link" :class="{active: i == selectedIndex, 'nav-link-horizontal':isHorizontal}" 
                    @click="onClicked(i, option)" aria-current="page" 
                    :style="styleObjectToString(styles['nav-link']) + styleObjectToString(styles['nav-link-selected'], i == selectedIndex)">
                        <i class="icon" :class="icons[i]" :style="styleObjectToString(styles['icon'])"></i>
                        {{option}}
                    </a>
                </li>
            </ul>
        </div>
    </div>
</template>
<script>
import { ref } from "vue"
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-icons/font/bootstrap-icons.css";


function getFullIconName(name) {
    return name.slice(0,3) !== "bi-"? "bi-" + name : name
}

export default {
    name: "MyComponent",
    props: ["args"], // Arguments that are passed to the plugin in Python are accessible in prop "args"
    setup(props) {
        useStreamlit() // lifecycle hooks for automatic Streamlit resize

        const menuTitle = ref(props.args.menuTitle)
        const isHorizontal = props.args.orientation == "horizontal"
        const menuIcon = ref(props.args.menuIcon || "bi-menu-up")
        menuIcon.value = getFullIconName(menuIcon.value)
        const icons = ref(props.args.icons || [])
        for (let i = 0; i < props.args.options.length; i++) {
            if (!icons.value[i]) {
                icons.value[i] = "bi-caret-right";
            }
            icons.value[i] = getFullIconName(icons.value[i]);
        }
        const selectedIndex = ref(props.args.defaultIndex)
        const onClicked = (index, option) => {
            selectedIndex.value = index
            Streamlit.setComponentValue(option)
        }
        const styleObjectToString = (obj, condition) => {
            if (typeof condition === "undefined") {
                condition = true
            }
            if (!condition) {
                return ""
            }
            let styleString = ""
            for (const key in obj) {
                styleString += `${key}:${obj[key]};`
            }
            return styleString
        }
        const styles = ref(props.args.styles || {});
        return {
            selectedIndex,
            menuTitle,
            menuIcon,
            icons,
            styles,
            onClicked,
            styleObjectToString,
            isHorizontal
        }
    },
}
</script>

<style scoped>
.icon {
    font-size: 1rem;
    margin-right: 0.5rem;
}

.menu hr {
    margin-top: 0.5rem;
    margin-bottom: 0.5rem;
}

.menu .container-xxl {
   background-color: var(--secondary-background-color);
   border-radius: 0.5rem;
}

.menu-title {
    margin-left: 0.75rem;
    margin-right: 0.75rem;
}

.menu-title, .menu-title .icon {
    font-size: 1.5rem;
}

.menu-title .icon {
    margin-right: 0.75rem;
}

.menu-title, .menu .nav-link, .menu .nav-item, hr {
    color: var(--text-color);
}

.nav-link.active {
    color: white;
}

.nav-link:hover {
    background-color: var(--hover-color);
}

.nav-link-hover:hover {
    background-color: inherit;
}

.menu .nav-link {
    /* box-shadow: 0 0px 0.2rem #aaa; */
    margin-top: 0.25rem;
    margin-bottom: 0.25rem;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
}

.menu .nav-link-horizontal {
    /* margin-top: 0.25rem;
    margin-bottom: 0.25rem; */
    padding-top: 0.25rem;
    padding-bottom: 0.25rem;
}

.p-h {
    padding: 0.5rem 0.75rem;
}

.container .flex-column {
    padding-top: 0.25rem;
}

.menu .nav-item .nav-link.active{
    background-color: var(--primary-color);
}

.nav-link.active, .nav-link.active+.icon {
    font-weight: 900;
}

.vr {
    width: 1px; 
    height: 80%;
}
</style>