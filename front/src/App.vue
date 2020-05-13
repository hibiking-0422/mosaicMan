<template>
  <div id="app">
    <div class="content">
        <h1>File Upload</h1>
        <p><input type="file" name="image" v-on:change="fileSelected"></p>
        <button v-on:click="fileUpload">アップロード</button>
    </div>
    <img :src="dataUrl" />
  </div>
</template>

<script>


export default {
  name: 'App',
  data: function(){
        return {
          fileInfo: '',
          dataUrl: ""
        }
    },
  methods:{
    fileSelected(event){
        console.log(event)
        this.fileInfo = event.target.files[0]
    },
    fileUpload(){
        const formData = new FormData()

        formData.append('file',this.fileInfo)

        this.axios.post('http://localhost:5000/hoge',formData).then(response =>{
            this.dataUrl = "data:image/png;base64," + response.data
            console.log(this.dataUrl)
      });
    },
}

}
</script>

<style>
.content{
    margin:5em;
}
</style>
