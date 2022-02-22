<template>
  <div class="home">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
	<form>
		<div class="form-group">
			<label for="exampleFormControlInput1">Заголовок</label>
			<input v-model="post_body.title" class="form-control" type="text" placeholder="Default input">
		</div>
		
		<div class="form-group">
			<label for="exampleFormControlTextarea1">Текст</label>
			<textarea v-model="post_body.text" class="form-control" id="exampleFormControlTextarea1" rows="3"></textarea>
		</div>
		
		<div class="form-group">
			<label for="exampleFormControlSelect2">Темы</label>
			<select v-model="post_body.topic" multiple class="form-control" id="exampleFormControlSelect2">
			<option v-for="option in topics" :value="option.id" :key="option.id">
				{{ option.name }}
			</option>
			</select>
		</div>
		
		<div class="form-group">
			<label for="exampleFormControlSelect1">Язык</label>
			<select v-model="post_body.language" class="form-control" id="exampleFormControlSelect1">
				<option v-for="option in languages" :value="option.id" :key="option.id">
					{{ option.name }}
				</option>
			</select>
		</div>
		
		<div class="form-group">
			<label for="exampleFormControlSelect1">Источник</label>
			<select v-model="post_body.source" class="form-control" id="exampleFormControlSelect1">
				<option v-for="option in sources" :value="option.id" :key="option.id">
					{{ option.name }}
				</option>
			</select>
		</div>
		<input v-on:click="postData" class="btn btn-primary" value="Отправить">
		<p>{{ out_message }}</p>
	</form>
		{{ post_body.language }}
		{{ post_body.topic }}
  </div>
</template>

<script>
// @ is an alias to /src
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
export default {
	name: 'Home',
	components: {
		HelloWorld
	},
	data() {
		return {
			endpoint: 'http://localhost:55555/article/',
			post_body: {
				"title": "",
				"link": "/",
				"html_body": "",
				"text": "",
				"server_path": "/",
				"language": null,
				"source": null,
				"author": 1,
				"topic": [],
				
			},
			languages_end: 'http://localhost:55555/language/',
			sources_end: "http://localhost:55555/source/",
			topics_end: "http://localhost:55555/topic/",
			languages: null,
			sources: null,
			topics: null,
			out_message:  null,
		}
	},

	async created() {
		this.getAllData();
	},

	methods: {
		getData(endpoint) {
			return axios.get(endpoint)
				.then(response => {
				return response.data.results;
				})
			.catch(error => {
				console.log('-----error-------');
				console.log(error);
			})
		},
		async getAllData(){
			this.languages = await this.getData(this.languages_end);
			this.sources = await this.getData(this.sources_end);
			this.topics = await this.getData(this.topics_end);
		},
		postData() {
			this.post_body.html_body = this.post_body.text;
			for (const [key, value] of Object.entries(this.post_body)) {
				console.log(key, value);
				if (!value) {
					this.out_message = "Ошибка";
					return;
				}
			}
			axios.post(this.endpoint, this.post_body)
				.then(response => {
				console.log(response.data);
				this.out_message = "Отправлено";
				})
			.catch(error => {
				console.log('-----error-------');
				console.log(error);
				this.out_message = "Ошибка";
			})
		},
	}
}
</script>

<style>
.search-bar{
margin-left: 10%;
margin-top: 50px;
width: 800px;
display: flex;
justify-content: space-between;
padding: 1em;
box-sizing: border-box;
}


.search-bar-logo{
width: 30%;
   margin-left: 0;
  height: 2em;
}

.search-bar-bar{
    width: 65%;
  height: 2em;
  margin-left: 1em;
  margin-right: 1em;
}

.search-bar-bar:hover {
    -webkit-box-shadow: 5px 5px 3px 3px rgba(0, 0, 0, 0.3);
    box-shadow: 5px 5px 3px 3px rgba(0, 0, 0, 0.3);
}


.logo {
height: 3em;
}

#search-button{
outline: none;
}

#search-input{
outline: none;
}
.list_element {
text-align: left;
margin-left: 50px;
font-size: x-large;
}
.list_element div {
text-align: left;
margin-left: 50px;
font-size: large;
}
form {
text-align: left;
margin-left: 50px;
font-size: large;
}
</style>
