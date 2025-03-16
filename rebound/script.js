document.querySelectorAll("li, p").forEach(el => {
  el.innerHTML = el.innerHTML.replace(/"\s*([^"]+?)\s*"/g, '$1');
});
