<template>
    <div class="menu">
        <div class="container d-flex flex-column flex-shrink-0 p-3">
            <a href="#" class="menu-title align-items-center mb-md-0 me-md-auto text-decoration-none">
                <i class="icon" :class="menuIcon" style="font-size:3rem;"></i>
                <span class="fs-4">{{menuTitle}}</span>
            </a>
            <hr>
            <ul href="#" class="nav nav-pills flex-column mb-auto">
                <li class="nav-item" v-for="(option,i) in args.options" :key="option">
                    <hr v-if="option === '---'">
                    <a v-else href="#" class="nav-link" :class="{active: i == selectedIndex}" 
                    @click="onClicked(i, option)" aria-current="page">
                        <i class="icon" :class="icons[i]"></i>
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

        const menuTitle = ref(props.args.menuTitle || "Menu")
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

        return {
            selectedIndex,
            menuTitle,
            menuIcon,
            icons,
            onClicked,
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
    margin-bottom: 1rem;
}

.menu .container {
   background-color: var(--secondary-background-color);
   border-radius: 0.5rem;
}

.menu-title, .menu .nav-link, .menu .nav-item, hr {
    color: var(--text-color);
}

.nav-link.active {
    color: white;
}

.menu .nav-link {
    /* box-shadow: 0 0px 0.2rem #aaa; */
    margin-bottom: 0.5rem;
    padding-top: 0.5rem;
    padding-bottom: 0.5rem;
}

.menu .nav-item .nav-link.active{
    background-color: var(--primary-color);
}

.nav-link.active, .nav-link.active+.icon {
    font-weight: 900;
}

</style>