<template>
  <div class="home">
    <HelloWorld msg="Welcome to Your Vue.js App"/>
	
	<div class="search-bar">
        <div class="search-bar-logo">
            TYNDEX
        </div>
        <div class="search-bar-bar">
			<div class="input-group mb-3">
				<input id="input-search" v-on:keyup.enter="refresh" v-model="query" type="text" class="form-control" placeholder="Введите запрос" aria-label="jopa" aria-describedby="basic-addon2">
				<div class="input-group-append">
					<button id="button-search" class="btn btn-primary" type="button" title="Искать" v-on:click="refresh">
						<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
							<path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
						</svg>
					</button>
				</div>
			</div>
		</div>
    </div>
	<div v-show="count"> Найдено: {{count}}</div>
		<router-link 
        v-for="post in posts" :key="post.id"
        active-class="is-active"
        class="link"
        :to="{ name: 'post', params: { id: post.id } }">
			<li class="list_element">{{post.title}}<div>{{post.posted}}</div></li>
		</router-link>
		
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
			posts: null,
			endpoint: 'http://localhost:55555/article/?text=',
			query: '',
			count: null,
		}
	},

	created() {
		this.refresh();
	},

	methods: {
		refresh() {
			if (this.query) {
				axios.get(this.endpoint + this.query)
					.then(response => {
					this.posts = response.data;
					this.count = this.posts.length;
					})
				.catch(error => {
					console.log('-----error-------');
					console.log(error);
				})
			}
		}
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
</style>
