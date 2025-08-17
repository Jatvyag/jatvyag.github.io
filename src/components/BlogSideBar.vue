<template>
  <aside class="blog-sidebar">
    <!-- Search -->
    <input
      v-model="searchQuery"
      type="text"
      :placeholder="t('blog.search') + '...'"
      class="search-input"
    >
    <!-- Categories -->
    <div>
      <h2 class="sidebar-heading">
        {{ t('blog.categories') }}
      </h2>
      <ul
        v-if="props.categories.length"
        class="category-list"
      >
        <li
          v-for="cat in props.categories"
          :key="cat"
          class="sidebar-item"
          @click="selectedCategory = cat"
        >
          {{ cat }}
        </li>
      </ul>
      <p
        v-else
        class="no-results"
      >
        <font-awesome-icon :icon="['fas', 'ghost']" />
        {{ t('blog.no_match') }}
      </p>
      <template v-if="selectedCategory">
        <font-awesome-icon :icon="['fas', 'filter-circle-xmark']" />
        <span
          class="sidebar-reset"
          @click="selectedCategory = null"
        >
          {{ t('blog.reset') }}
        </span>
      </template>
    </div>
    <!-- Tags -->
    <div>
      <h2 class="sidebar-heading">
        {{ t('blog.tags') }}
      </h2>
      <div
        v-if="props.tags.length"
        class="tag-cloud"
      >
        <span
          v-for="tag in props.tags"
          :key="tag"
          class="tag blog"
          @click="selectedTag = tag"
        >
          {{ tag }}
        </span>
      </div>
      <p
        v-else
        class="no-results"
      >
        <font-awesome-icon :icon="['fas', 'ghost']" />
        {{ t('blog.no_match') }}
      </p>
      <template v-if="selectedTag">
        <font-awesome-icon :icon="['fas', 'filter-circle-xmark']" />
        <span
          class="sidebar-reset"
          @click="selectedTag = null"
        >
          {{ t('blog.reset') }}
        </span>
      </template>
    </div>
    <!-- Types -->
    <div>
      <h2 class="sidebar-heading">
        {{ t('blog.types') }}
      </h2>
      <div
        v-if="props.types.length"
        class="type-icons"
      >
        <img
          v-for="type in props.types"
          :key="type.name"
          :src="props.getIconPath(type.icon)"
          :alt="type.name"
          :title="type.name"
          class="type-icon"
          @click="selectedType = type.name"
        >
      </div>
      <p
        v-else
        class="no-results"
      >
        <font-awesome-icon :icon="['fas', 'ghost']" />
        {{ t('blog.no_match') }}
      </p>
      <template v-if="selectedType">
        <font-awesome-icon :icon="['fas', 'filter-circle-xmark']" />
        <span
          class="sidebar-reset"
          @click="selectedType = null"
        >
          {{ t('blog.reset') }}
        </span>
      </template>
    </div>
  </aside>
</template>

<script setup>
import { useI18n } from 'vue-i18n'
const { t } = useI18n()

const searchQuery = defineModel('searchQuery', { type: String })
const selectedCategory = defineModel('selectedCategory', { type: String, default: null })
const selectedTag = defineModel('selectedTag', { type: String, default: null })
const selectedType = defineModel('selectedType', { type: String, default: null })

const props = defineProps({
  categories: {
    type: Array,
    required: true
  },
  tags: {
    type: Array,
    required: true
  },
  types: {
    type: Array,
    required: true
  },
  getIconPath: {
    type: Function,
    required: true
  }
})
</script>

<style lang="scss" scoped>
.blog-sidebar {
  display: flex;
  flex-direction: column;
  border-radius: 10px;
  border: 2px solid var(--card-shadow);
  box-shadow: var(--card-shadow);
  background-color: var(--blog-sidebar);
  gap: 1.5rem;
  padding: 1rem;
}

.search-input {
  padding: 0.5rem;
  border: 1px solid transparent;
  border-radius: 10px;
}

.search-input:focus {
  outline: none;
  box-shadow: 0 0 0 4px var(--btn-hover);
}

.sidebar-heading {
  font-weight: bold;
  font-size: 1.5rem;
  text-align: left;
  margin-top: 0.5rem;
  margin-bottom: 1rem;
}

.category-list {
  display: flex;
  gap: 1rem;
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
  border-color: var(--btn-hover);
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

.no-results {
  text-align: center;
  color: #888;
}
</style>
