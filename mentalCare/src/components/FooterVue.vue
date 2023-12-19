<script setup lang="ts">
    defineProps<{ footer: string }>()
</script>

<template>
  <div class="footer_div">
    <p class="footer_p">{{ footer }}</p>
  </div>
</template>