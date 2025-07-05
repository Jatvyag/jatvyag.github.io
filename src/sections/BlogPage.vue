<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import BlogPostCard from '../components/BlogPostCard.vue'
import jsonENPostsData from '../data/posts_en.json'
import jsonBEPostsData from '../data/posts_be.json'

const skillIcons = import.meta.glob('../assets/icons/*', {
  eager: true,
  import: 'default',
  query: '?url',
})

const { t, locale } = useI18n()
const props = defineProps({
  sectionLink: {
    type: String,
    required: true,
  },
})

const searchQuery = ref('')
const selectedCategory = ref(null)
const selectedTag = ref(null)
const selectedType = ref(null)
const currentPage = ref(1)
const postsPerPage = 10

const posts = computed(() => {
  return locale.value === 'be' ? jsonBEPostsData.posts : jsonENPostsData.posts
})

// Filtered and paginated posts
const filteredPosts = computed(() =>
  posts.value.filter(post => {
    const matchesSearch =
      post.title.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
      post.desc.toLowerCase().includes(searchQuery.value.toLowerCase())

    const matchesCategory = !selectedCategory.value || post.cat === selectedCategory.value
    const matchesTag = !selectedTag.value || post.tag.includes(selectedTag.value)
    const matchesType = !selectedType.value || post.type.name === selectedType.value

    return matchesSearch && matchesCategory && matchesTag && matchesType
  })
)

const paginatedPosts = computed(() => {
  const start = (currentPage.value - 1) * postsPerPage
  return filteredPosts.value.slice(start, start + postsPerPage)
})

// Extract unique values
const categories = computed(() => [...new Set(posts.value.map(p => p.cat))])
const tags = computed(() => [...new Set(posts.value.flatMap(p => p.tag))])
const types = computed(() => [...new Set(posts.value.map(p => p.type.name))])

function getIconPath(iconName) {
  return skillIcons[`../assets/icons/${iconName.toLowerCase()}.svg`]
}
</script>

<template>
  <section :id="props.sectionLink.replace('#', '')" class="blog-section">
    <h1 class="blog">{{ t('blog.title') }}</h1>
    <div class="blog-grid">
      <!-- Sidebar -->
      <aside class="blog-sidebar">
        <!-- Search -->
        <input
          v-model="searchQuery"
          type="text"
          :placeholder="t('blog.search') + '...'"
          class="search-input"
        />

        <!-- Categories -->
        <div>
          <h2 class="sidebar-heading">{{ t('blog.categories') }}</h2>
          <ul class="category-list">
            <li
              v-for="cat in categories"
              :key="cat"
              class="sidebar-item"
              @click="selectedCategory = cat"
            >
              {{ cat }}
            </li>
          </ul>
          <span class="sidebar-reset" @click="selectedCategory = null">{{ t('blog.reset') }}</span>
        </div>

        <!-- Tags -->
        <div>
          <h2 class="sidebar-heading">{{ t('blog.tags') }}</h2>
          <div class="tag-cloud">
            <span
              v-for="tag in tags"
              :key="tag"
              class="tag blog"
              @click="selectedTag = tag"
            >
              {{ tag }}
            </span>
          </div>
          <span class="sidebar-reset" @click="selectedTag = null">{{ t('blog.reset') }}</span>
        </div>

        <!-- Types -->
        <div>
          <h2 class="sidebar-heading">{{ t('blog.types') }}</h2>
          <div class="type-icons">
            <img
              v-for="type in types"
              :key="type"
              :src="getIconPath(type)"
              :alt="type"
              :title="type"
              class="type-icon"
              @click="selectedType = type"
            />
          </div>
          <span class="sidebar-reset" @click="selectedType = null">{{ t('blog.reset') }}</span>
        </div>
      </aside>

      <!-- Post List -->
      <div class="blog-posts">
        <template v-if="paginatedPosts.length">
          <BlogPostCard
            v-for="post in paginatedPosts"
            :key="post.id"
            :post="post"
          />
        </template>
        <template v-else>
          <BlogPostCard
            :post="{
              title: t('blog.noResults') || 'No posts match your search.',
              desc: '',
              tag: [],
              libs: [],
              cat: '',
              date: '',
              link: '',
              pic: ''
            }"
            :empty="true"
          />
        </template>

        <!-- Pagination -->
        <div v-if="filteredPosts.length > postsPerPage" class="pagination">
          <button
            class="page-btn"
            :disabled="currentPage === 1"
            @click="currentPage--"
          >
            {{ t('blog.prev') }}
          </button>
          <span class="page-number">{{ currentPage }}</span>
          <button
            class="page-btn"
            :disabled="currentPage * postsPerPage >= filteredPosts.length"
            @click="currentPage++"
          >
            {{ t('blog.next') }}
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.blog-section {
  padding: 2rem;
  max-width: 1200px;
}

h1.blog {
  font-size: 3rem;
  margin-bottom: 2rem;
}

.blog-grid {
  display: grid;
  grid-template-columns: 1fr 4fr;
  align-items: start;
  gap: 2rem;
}

/* Sidebar */
.blog-sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.search-input {
  padding: 0.5rem;
  border: 1px solid transparent;
  border-radius: var(--border-radius);
}

.search-input:focus {
  outline: none;
  box-shadow: 0 0 0 4px var(--btn-hover-color);
}

.sidebar-heading {
  font-weight: bold;
  font-size: 1.5rem;
  text-align: left;
  margin-top: 0.5rem;
  margin-bottom: 1rem;
}

.category-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar-item {
  display: inline-block;
  padding: 0.25rem;
  color: var(--link);
  cursor: pointer;
  padding: 0.25rem 0;
}

.sidebar-item:hover {
  color: var(--link-hover);
}

.sidebar-item:active {
  color: var(--link-active);
  transform: scale(0.95);
}

.sidebar-reset {
  display: inline-block;
  padding: 0.25rem;
  color: #999;
  font-size: 0.875rem;
  cursor: pointer;
  margin-top: 0.5rem;
}

.sidebar-reset:hover {
  color: var(--link-hover);
}

.sidebar-reset:active {
  transform: scale(0.95);
}

.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag.blog {
  cursor: pointer;
  border: 2px solid transparent;
}

.tag.blog:hover {
  cursor: pointer;
  border-color: var(--btn-hover-color);
}

.tag.blog:active {
  transform: scale(0.95);
}

.type-icons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
}

.type-icon {
  width: 36px;
  height: 36px;
  cursor: pointer;
  transition: transform 0.2s ease;
}

.type-icon:hover {
  transform: scale(1.1);
}

/* Posts */
.blog-posts {
  display: flex;
  flex-direction: column;
  min-width: 0;
  gap: 1.5rem;
}

/* Pagination */
.pagination {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
  align-items: center;
}

.page-btn {
  cursor: pointer;
}

.page-btn:disabled {
  border: 2px solid transparent;
  transform: scale(1);
  opacity: 0.5;
  cursor: not-allowed;
}

.page-number {
  font-size: 1.2rem;
}

.no-results {
  padding: 2rem;
  text-align: center;
  width: 100px;
  color: #888;
  font-style: italic;
}

@media (max-width: 800px) {
  h1.blog {
    font-size: 2rem;
  }

  .blog-grid {
    grid-template-columns: 1fr; /* Stack items vertically */
  }

  .pagination {
    justify-content: center;
  }
}
</style>
