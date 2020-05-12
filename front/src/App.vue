<template>
  <div id="app">
    <div class="content">
        <h1>File Upload</h1>
        <p><input type="file" v-on:change="fileSelected"></p>
        <button v-on:click="fileUpload">アップロード</button>
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
  data: function(){
        return {
          fileInfo: ''
        }
    },
  methods:{
        fileSelected(event){
            console.log(event)
            this.fileInfo = event.target.files[0]
        }
    },
    fileUpload(){
      const formData = new FormData()

      formData.append('file',this.fileInfo)

      this.axios.post('/api/fileupload',formData).then(response =>{
          console.log(response)
    });
}

}
</script>

<style>
.content{
    margin:5em;
}
</style>
