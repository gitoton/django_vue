<script setup lang="ts">
    defineProps<{ header: string }>()
</script>

<template>
  <!-- <div class="header_p">
    <p class="header_p">{{ header }}</p>
  </div> -->
  <header class="mb-auto">
    <nav class="navbar navbar-expand navbar-dark bg-dark justify-content-between">
      <h1><span class="navbar-brand mb-0 h1">It's {{ header }} !!</span></h1>
    </nav>
  </header>
</template>