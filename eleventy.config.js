export default function (eleventyConfig) {
  // Copy static assets straight through to the built site
  eleventyConfig.addPassthroughCopy({ "src/css": "css" });
  eleventyConfig.addPassthroughCopy({ "src/CNAME": "CNAME" });

  // Human-readable date, e.g. "14 April 2026"
  eleventyConfig.addFilter("readableDate", (dateObj) => {
    return new Date(dateObj).toLocaleDateString("en-GB", {
      day: "numeric",
      month: "long",
      year: "numeric",
    });
  });

  // ISO date for <time> elements, sitemaps and JSON-LD
  eleventyConfig.addFilter("isoDate", (dateObj) => {
    return new Date(dateObj).toISOString().split("T")[0];
  });

  // Scheduled posts: a post dated in the future is left out of the build
  // until its date arrives (the deploy workflow rebuilds daily to pick it up).
  // Local dev server (npm start) still shows them so you can preview.
  eleventyConfig.addPreprocessor("scheduled-posts", "md", (data) => {
    if (process.env.ELEVENTY_RUN_MODE === "serve") return;
    if (data.page?.inputPath?.includes("/posts/") && data.page.date > new Date()) {
      return false;
    }
  });

  // Newest posts first
  eleventyConfig.addCollection("posts", (collectionApi) => {
    return collectionApi
      .getFilteredByGlob("src/posts/*.md")
      .sort((a, b) => b.date - a.date);
  });

  return {
    dir: {
      input: "src",
      includes: "_includes",
      data: "_data",
      output: "_site",
    },
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
}
