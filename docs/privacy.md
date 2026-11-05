# Privacy and external services

This documentation is hosted by GitHub Pages at [fair-dama.perdl.com](https://fair-dama.perdl.com/). Visiting the site sends a normal web request to its host. GitHub's hosting practices are outside the site's cookie settings.

For current browsers, the site's theme styles, scripts, images, and favicon are served from the documentation domain, and text uses system fonts. It does not configure analytics or advertising.

The repository link opens GitHub only when you select it. The optional **GitHub repository details** setting allows the theme to request public repository information, such as stars or releases, from GitHub. It starts unchecked. You can accept, reject, or manage this setting in the consent dialog, and reopen the dialog with **Change cookie settings** in the footer.

The theme stores site preferences and your consent choice in your browser's local storage. These controls cover optional requests made by this site; they do not control GitHub Pages hosting or requests you initiate by following an external link.

## Request inventory

- **GitHub Pages:** Serves the documentation and its assets from `fair-dama.perdl.com`. These hosting requests are required to view the site.
- **GitHub:** The repository link is user-initiated. The theme's GitHub API requests for repository details are conditional on the optional GitHub setting, which starts unchecked.
- **Interactive Sankey diagram:** Its static SVG preview is local. Selecting **Load interactive diagram** or opening the standalone page loads the packaged viewer in an iframe. That viewer requests D3 and d3-sankey from jsDelivr and viewer libraries from unpkg; the package may use other external viewer assets. The embedded reading copy opens in a new tab only when a diagram label is selected. The diagram is not loaded automatically and does not use the site's cookie setting as its trigger.
- **Google Fonts and analytics:** Neither is configured for the documentation theme. The theme uses system fonts and local site assets in current browsers.
- **Theme fallbacks:** The bundled theme contains code that can load a ResizeObserver polyfill from `unpkg.com` in browsers without native support. It also contains a lightbox loader for pages using that feature; this site has no lightbox content. Browser compatibility and replacement of these fallbacks remain service decisions if support for older browsers is required.

The consent controls limit the site's optional GitHub API requests. They do not, by themselves, establish compliance with any particular privacy law.
