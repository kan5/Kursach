<template>
	<div class="about">
		<HelloWorld msg="Welcome to Your Vue.js App"/>
		<div class="post" v-if="post">
			<h1 class="post__title">{{ post.title }}</h1>
			<div id="post_view" class="post__html_body" v-html="post.html_body"></div>
		</div>
	</div>
</template>

<script>
import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'

export default {
	name: 'post',
	components: {
		HelloWorld
	},
	props: ['id'],
	data() {
		return {
			post: null,
			endpoint: 'http://localhost:55555/article/',
		}
	},

	created() {
		this.refresh(this.id);
	},

	methods: {
		refresh(id) {
			if (id) {
				axios.get(this.endpoint + id)
					.then(response => {
					this.post = response.data;
					})
				.catch(error => {
					console.log('-----error-------');
					console.log(error);
				})
			}
		}
	},
	
}
</script>

<style>
#post_view {
text-align: left;
margin-left: 20px;
white-space: pre;
}
</style>
