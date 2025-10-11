export function getAssetHref (dir, badgeFile) {
  return new URL(`../assets/${dir}/${badgeFile}`, import.meta.url).href
}
