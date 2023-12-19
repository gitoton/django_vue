<script setup lang="ts">
  import { ref } from 'vue'
  defineProps<{ contents: string }>()

  const emotions_header = ref("感情")
  const thinkings_header = ref("考え")
  const behaviors_header = ref("行動")
  const feelings_header = ref("身体感覚")

  const emotion_content = ref("")
  const thinking_content = ref("")
  const behavior_content = ref("")
  const feeling_content = ref("")

  const emotions_contents = ref<string[]>([])
  const thinkings_contents = ref<string[]>([])
  const behaviors_contents = ref<string[]>([])
  const feelings_contents = ref<string[]>([])

  function add_emotions_contents(){
    if(emotion_content.value != ""){
      emotions_contents.value.push(emotion_content.value)
      emotion_content.value = ""
    }
  }

  function delete_emotions_contents(index: number){
    emotions_contents.value.splice(index, 1)
  }

  function add_thinkings_contents(){
    if(thinking_content.value != ""){
      thinkings_contents.value.push(thinking_content.value)
      thinking_content.value = ""
    }
  }

  function delete_thinkings_contents(index: number){
    thinkings_contents.value.splice(index, 1)
  }

  function add_behaviors_contents(){
    if(behavior_content.value != ""){
      behaviors_contents.value.push(behavior_content.value)
      behavior_content.value = ""
    }
  }

  function delete_behaviors_contents(index: number){
    behaviors_contents.value.splice(index, 1)
  }

  function add_feelings_contents(){
    if(feeling_content.value != ""){
      feelings_contents.value.push(feeling_content.value)
      feeling_content.value = ""
    }
  }

  function delete_feelings_contents(index: number){
    feelings_contents.value.splice(index, 1)
  }

</script>

<template>
  <!-- <div class="contents_p">
    <p class="contents_p">{{ contents }}</p>
  </div> -->
  <div class="card">
    <div class="emotions mental-monitoring-content gradient">
      <p class="mental-monitoring-content-caption">{{ emotions_header }}</p>
      <input class="input input_emotions" type="text" v-model="emotion_content" v-on:keydown.enter="add_emotions_contents">
      <li class="mental-monitoring-content-li" v-for="(emotion, index) in emotions_contents" :key="index">
        <p class="mental-monitoring-content-string">{{ emotion }}</p>
        <button class="delete-button emotion_delete" @click="delete_emotions_contents(index)">×</button>
      </li>
    </div>
    <div class="thinkings mental-monitoring-content gradient">
      <p class="mental-monitoring-content-caption">{{ thinkings_header }}</p>
      <input class="input input_thinkings" type="text" v-model="thinking_content" v-on:keydown.enter="add_thinkings_contents">
      <li class="mental-monitoring-content-li" v-for="(thinking, index) in thinkings_contents" :key="index">
        <p class="mental-monitoring-content-string">{{ thinking }}</p>
        <button class="delete-button delete_thinkings" @click="delete_thinkings_contents(index)">×</button>
      </li>
    </div>
  </div>
  <div class="card">
    <div class="behaviors mental-monitoring-content gradient">
      <p class="mental-monitoring-content-caption">{{ behaviors_header }}</p>
      <input class="input input_behaviors" type="text" v-model="behavior_content" v-on:keydown.enter="add_behaviors_contents">
      <li class="mental-monitoring-content-li" v-for="(behavior, index) in behaviors_contents" :key="index">
        <p class="mental-monitoring-content-string">{{ behavior }}</p>
        <button class="delete-button delete_behaviors" @click="delete_behaviors_contents(index)">×</button>
      </li>
    </div>
    <div class="feelings mental-monitoring-content gradient">
      <p class="mental-monitoring-content-caption">{{ feelings_header }}</p>
      <input class="input input_feelings" type="text" v-model="feeling_content" v-on:keydown.enter="add_feelings_contents">
      <li class="mental-monitoring-content-li" v-for="(feeling, index) in feelings_contents" :key="index">
        <p class="mental-monitoring-content-string">{{ feeling }}</p>
        <button class="delete-button delete_feelings" @click="delete_feelings_contents(index)">×</button>
      </li>
    </div>
  </div>
</template>

<style scoped>
.gradient {
  /* height: 200px; */
  width: 100%;
  background-image: linear-gradient(90deg, rgba(251, 213, 251, 1), rgba(149, 233, 243, 1));
  border-radius: 8px;
  padding: 4px;
  margin: 1px;
  /* display: inline-block; */
}

 .mental-monitoring-content {
  width: 400px;
  height: 250px;
  border: 4px;
  display: inline-block;
}

.mental-monitoring-content-caption {
  font-size: 1.8rem;
  font-weight: bold;
  padding: 1px;
  color: #383838;
  margin: 2px;
}

.input {
  margin-bottom: 5px;
  width: calc(100% - 1.5em);
  border-bottom: 1px;
  background-color: aliceblue;
  border: 1px;
  color: #383838;
}

.mental-monitoring-content-string .mental-monitoring-content-list {
  color: #383838;
}

.mental-monitoring-content-string {
  margin: .1px;
  display: inline-block;
  max-width: 400;
}

.delete-button {
  margin-left: 10px;
  background-color: rgba(244, 120, 120, 10);
  color: #383838;
  width: 25px;
}

</style>