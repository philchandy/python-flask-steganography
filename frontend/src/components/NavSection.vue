<template>
    <fwb-navbar solid class="bg-black">
      <template #logo>
        <h2 class="text-white font-bold tracking-widest text-xl">StegSafe</h2>
      </template>
      <template  #default="{isShowMenu}">
        <fwb-navbar-collapse :is-show-menu="isShowMenu">
          <fwb-navbar-link link="/" class="text-white">
            Home
          </fwb-navbar-link>
          <fwb-navbar-link link="/hide-text" class="text-white">
            Hide Text
          </fwb-navbar-link>
          <fwb-navbar-link link="/extract-text" class="text-white">
            Extract Text
          </fwb-navbar-link>
        </fwb-navbar-collapse>
      </template>
    </fwb-navbar>
  </template>
  
  <script setup>
  import {
    FwbNavbar,
    FwbNavbarCollapse,
    FwbNavbarLink,
  } from 'flowbite-vue'
  </script>