<script setup lang="ts">
import HeaderVue from './components/HeaderVue.vue'
import ContentsVue from './components/ContentsVue.vue'
import FooterVue from './components/FooterVue.vue'

</script>

<template>
  <dev class="body">
    <HeaderVue header="Menta" />
    <ContentsVue contents="fugafuga" />
    <FooterVue footer="ponpon" />
  </dev>
</template>

<style scoped>
.body {
   background-color: #ffaaaa;
}
</style>
