<template>
  <main class="blog">
    <section
      id="home"
      class="blog-section"
    >
      <h1 class="blog">
        {{ t('blog.title') }}
      </h1>
      <div class="blog-grid">
        <BlogSidebar
          v-model:search-query="searchQuery"
          v-model:selected-category="selectedCategory"
          v-model:selected-tag="selectedTag"
          v-model:selected-type="selectedType"
          :categories="categories"
          :tags="tags"
          :types="types"
          :get-icon-path="getIconPath"
        />
        <!-- Post List -->
        <div class="blog-posts">
          <template v-if="paginatedPosts.length">
            <BlogPostCard
              v-for="post in paginatedPosts"
              :key="post.id"
              :post="post"
              :empty="false"
            />
          </template>
          <template v-else>
            <BlogPostCard
              :post="emptyCard"
              :empty="true"
            />
          </template>
          <!-- Pagination -->
          <div
            v-if="filteredPosts.length > postsPerPage"
            class="pagination"
          >
            <button
              class="page-btn"
              :disabled="prevBtnDisabled"
              :title="t('blog.prev')"
              @click="currentPage--"
            >
              <font-awesome-icon
                :icon="['fas', 'backward-step']"
              />
            </button>
            <span class="page-number">{{ currentPage }}</span>
            <button
              class="page-btn"
              :disabled="nextBtnDisabled"
              :title="t('blog.next')"
              @click="currentPage++"
            >
              <font-awesome-icon
                :icon="['fas', 'forward-step']"
              />
            </button>
          </div>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import { useNavStore } from '@/stores/nav'
import { useI18n } from 'vue-i18n'
import BlogPostCard from '@/components/BlogPostCard.vue'
import BlogSidebar from '@/components/BlogSideBar.vue'
import jsonENPostsData from '@/data/posts_en.json'
import jsonBEPostsData from '@/data/posts_be.json'

const nav = useNavStore()
nav.setNavItems([
  { key: 'home', link: '#home', faIcon: ['fas', 'house'], type: 'main_menu', disabled: true }
])
nav.setCurrentSection('home')
nav.setMainSection(getLinkByKey('home'))
nav.setNavMenuLocale('navMenu.blog')

function getLinkByKey (key) {
  const item = nav.navItems.find(i => i.key === key)
  return item?.link || ''
}

const skillIcons = import.meta.glob('../assets/icons/*', {
  eager: true,
  import: 'default',
  query: '?url'
})

const { t, locale } = useI18n()

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
  posts.value.slice().reverse().filter(post => {
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

// Extract unique filter values from posts
const categories = computed(() => {
  return [...new Set(filteredPosts.value.map(p => p.cat))]
})

const tags = computed(() => {
  return [...new Set(filteredPosts.value.flatMap(p => p.tag))]
})

const types = computed(() => {
  return [...new Set(filteredPosts.value.map(p => p.type.name))]
})

// Reset pagination when filter values change
watch([searchQuery, selectedCategory, selectedTag, selectedType], () => {
  currentPage.value = 1
})

// Get icons for filter values
function getIconPath (iconName) {
  return skillIcons[`../assets/icons/${iconName.toLowerCase()}.svg`]
}

const emptyCard = computed(() => {
  return {
    title: t('blog.noResults'),
    desc: '',
    tag: [],
    libs: [],
    cat: '',
    date: '',
    link: '',
    pic: ''
  }
})

// Pagination buttons
const prevBtnDisabled = computed(() => {
  return currentPage.value === 1
})

const nextBtnDisabled = computed(() => {
  return currentPage.value * postsPerPage >= filteredPosts.value.length
})
</script>

<style lang="scss" scoped>
main.blog {
  display: flex;
  flex-flow: column;
  align-items: center;
}

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
