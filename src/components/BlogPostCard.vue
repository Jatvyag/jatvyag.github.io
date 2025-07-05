<script setup>
const props = defineProps({
    post: {
        type: Object,
        required: true
    }
})

const thumbnails = import.meta.glob('../assets/blog/thumbs/*', { eager: true, query: '?url', import: 'default' })

const skillIcons = import.meta.glob('../assets/skills/*', { eager: true, query: '?url', import: 'default' })

function getThumb(path) {
    return thumbnails[`../assets/blog/thumbs/${path}`]
}

function getIcon(path) {
    return skillIcons[`../assets/skills/${path}`]
}
</script>

<template>
    <div class="blog-card">
        <!-- Image -->
        <img
        :src="getThumb(post.pic)"
        alt="Project image"
        class="blog-thumb"
        />

        <!-- Info -->
        <div class="blog-info">
        <h3 class="post-title">{{ post.title }}</h3>
        <p class="post-desc">{{ post.desc }}</p>
        <p class="post-cat">{{ post.cat }}</p>

        <!-- Tags -->
        <div class="post-tags">
            <span
            v-for="tag in post.tag"
            :key="tag"
            class="tag"
            >
            {{ tag }}
            </span>
        </div>

        <!-- Libs -->
        <div class="post-libs">
            <img
            v-for="lib in post.libs"
            :key="lib.id"
            :src="getIcon(lib.icon)"
            :alt="lib.name"
            :title="lib.name"
            class="icon-img"
            />
        </div>

        <!-- Link -->
        <div class="post-link">
            <a
            v-if="post.link"
            :href="post.link"
            target="_blank"
            >
            View Project
            </a>
            <span v-else>No link available</span>
        </div>
        </div>
    </div>
</template>

<style scoped>
.blog-card {
    display: flex;
    gap: 1rem;
    border: 1px solid #ccc;
    padding: 1rem;
    border-radius: 6px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: box-shadow 0.2s ease;
}
.blog-card:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.blog-thumb {
    width: 160px;
    height: 128px;
    object-fit: cover;
    border-radius: 4px;
    flex-shrink: 0;
}

.blog-info {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.post-title {
    font-size: 1.25rem;
    font-weight: bold;
    margin: 0;
}

.post-desc {
    font-size: 0.875rem;
    color: #555;
    margin: 0;
}

.post-cat {
    font-size: 0.75rem;
    color: #2563eb; /* blue-600 */
}

.post-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    font-size: 0.75rem;
}

.tag {
    background-color: #e5e7eb; /* gray-200 */
    border-radius: 4px;
    padding: 0.25rem 0.5rem;
}

.post-libs {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 0.25rem;
}

.icon-img {
    width: 24px;
    height: 24px;
    object-fit: contain;
    display: block;
}

.post-link {
    margin-top: 0.5rem;
    font-size: 0.875rem;
}

.post-link a {
    color: #2563eb;
    text-decoration: underline;
}

.post-link span {
    color: #999;
}
</style>


