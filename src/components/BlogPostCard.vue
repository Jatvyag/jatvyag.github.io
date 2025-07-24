<template>
  <div
    v-if="empty"
    class="card blog empty-card"
  >
    <p class="empty-message">
      {{ post.title }}
    </p>
  </div>
  <div
    v-else
    class="card blog"
  >
    <!-- Image -->
    <div class="thumb-info">
      <img
        :src="getThumb(post.pic)"
        alt="Project image"
        class="blog-thumb"
      >
      <p class="post-cat">
        {{ localize(post.cat, locale) }}
      </p>
      <p class="post-cat">
        {{ post.date }}
      </p>
    </div>
    <!-- Info -->
    <div class="blog-info">
      <component
        :is="post.link ? 'router-link' : 'div'"
        :to="post.link ? `/${routePrefix}/${encodeURIComponent(post.link)}` : undefined"
      >
        <h3 class="post-title">
          {{ localize(post.title, locale) }}
        </h3>
      </component>
      <p class="post-desc">
        {{ localize(post.desc, locale) }}
      </p>
      <!-- Tags -->
      <div class="post-tags">
        <span
          v-for="tag in localize(post.tag, locale)"
          :key="tag"
          class="tag blog"
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
        >
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()

const { post, empty, localize } = defineProps({
  post: {
    type: Object,
    required: true
  },
  empty: {
    type: Boolean,
    default: false
  },
  localize: {
    type: Function,
    required: true
  }
})

const thumbnails = import.meta.glob(
  '../assets/thumbs/*',
  { eager: true, query: '?url', import: 'default' }
)

const skillIcons = import.meta.glob(
  '../assets/icons/*',
  { eager: true, query: '?url', import: 'default' }
)

function getThumb (path) {
  return thumbnails[`../assets/thumbs/${path}`]
}

function getIcon (path) {
  return skillIcons[`../assets/icons/${path}`]
}

const routePrefix = computed(() => {
  const type = post?.type?.name?.toLowerCase()
  switch (type) {
  case 'jupyter': return 'jupyter'
  case 'md': return 'md'
  default: return ''
  }
})
</script>

<style lang="scss" scoped>
.card.blog {
    display: flex;
    gap: 1rem;
    padding: 1rem;
}

.card.blog:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

.blog-thumb {
    width: 160px;
    height: 128px;
    object-fit: cover;
    border-radius: $border-radius;
}

.blog-info {
    display: flex;
    flex-direction: column;
    min-width: 0;
    gap: 0.5rem;
}

.post-title {
    font-size: 1.25rem;
    margin: 0;
}

.post-desc {
    font-size: 0.875rem;
    margin: 0;
}

.post-cat {
    font-size: 0.75rem;
}

.post-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    font-size: 0.75rem;
}

.tag.blog {
    border: 2px solid var(--btn-hover-color)
}

.post-libs {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-top: 0.25rem;
}

.icon-img {
    width: 36px;
    height: 36px;
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

.empty-card {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 150px;
    border: 2px dashed #ccc;
    color: #999;
    font-size: 1rem;
    text-align: center;
}

@media (max-width: 800px) {
    .card.blog {
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    .blog-thumb {
        width: 100%;
        height: auto;
        max-width: 400px;
    }

    .thumb-info {
        order: 2;
    }

    .blog-info {
        align-items: center;
        order: 1;
    }

    .post-tags,
    .post-libs {
        justify-content: center;
    }
}
</style>
