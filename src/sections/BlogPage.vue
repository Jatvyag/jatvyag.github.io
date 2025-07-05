<script setup>
import { ref, computed } from 'vue'
import { useI18n } from 'vue-i18n'
import BlogPostCard from '../components/BlogPostCard.vue'
import jsonENPostsData from '../data/posts_en.json'
import jsonBEPostsData from '../data/posts_be.json'

const skillIcons = import.meta.glob('../assets/skills/*', {
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
  return skillIcons[`../assets/skills/${iconName.toLowerCase()}.svg`]
}
</script>

<template>
  <section :id="props.sectionLink.replace('#', '')" class="blog-section">
    <h1 class="blog-title">{{ t('blog.title') }}</h1>

    <div class="blog-grid">
      <!-- Sidebar -->
      <aside class="blog-sidebar">
        <!-- Search -->
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search..."
          class="search-input"
        />

        <!-- Categories -->
        <div>
          <h2 class="sidebar-heading">Categories</h2>
          <ul class="category-list">
            <li
              v-for="cat in categories"
              :key="cat"
              class="sidebar-item"
              @click="selectedCategory = cat"
            >
              {{ cat }}
            </li>
            <li class="sidebar-reset" @click="selectedCategory = null">Reset</li>
          </ul>
        </div>

        <!-- Tags -->
        <div>
          <h2 class="sidebar-heading">Tags</h2>
          <div class="tag-cloud">
            <span
              v-for="tag in tags"
              :key="tag"
              class="tag"
              @click="selectedTag = tag"
            >
              {{ tag }}
            </span>
            <span class="tag-reset" @click="selectedTag = null">Reset</span>
          </div>
        </div>

        <!-- Types -->
        <div>
          <h2 class="sidebar-heading">Types</h2>
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
            <span class="type-reset" @click="selectedType = null">Reset</span>
          </div>
        </div>
      </aside>

      <!-- Post List -->
      <div class="blog-posts">
        <BlogPostCard
          v-for="post in paginatedPosts"
          :key="post.id"
          :post="post"
        />

        <!-- Pagination -->
        <div v-if="filteredPosts.length > postsPerPage" class="pagination">
          <button
            class="page-btn"
            :disabled="currentPage === 1"
            @click="currentPage--"
          >
            Prev
          </button>
          <span class="page-number">{{ currentPage }}</span>
          <button
            class="page-btn"
            :disabled="currentPage * postsPerPage >= filteredPosts.length"
            @click="currentPage++"
          >
            Next
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.blog-section {
  padding: 2rem;
}

.blog-title {
  text-align: center;
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 2rem;
}

.blog-grid {
  display: grid;
  grid-template-columns: 1fr 3fr;
  gap: 2rem;
}

/* Sidebar */
.blog-sidebar {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.search-input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #aaa;
  border-radius: 4px;
}

.sidebar-heading {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.category-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar-item {
  color: #2563eb;
  cursor: pointer;
  padding: 0.25rem 0;
}

.sidebar-reset {
  color: #999;
  font-size: 0.875rem;
  cursor: pointer;
  margin-top: 0.5rem;
}

.tag-cloud {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.tag {
  background: #e5e7eb;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.875rem;
  cursor: pointer;
}

.tag-reset {
  color: #999;
  font-size: 0.75rem;
  cursor: pointer;
  align-self: center;
}

.type-icons {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  align-items: center;
}

.type-icon {
  width: 24px;
  height: 24px;
  cursor: pointer;
  transition: transform 0.2s ease;
}
.type-icon:hover {
  transform: scale(1.1);
}

.type-reset {
  font-size: 0.75rem;
  color: #999;
  cursor: pointer;
}

/* Posts */
.blog-posts {
  display: flex;
  flex-direction: column;
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
  padding: 0.25rem 0.75rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  background: white;
  cursor: pointer;
}

.page-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.page-number {
  font-size: 0.875rem;
}
</style>
