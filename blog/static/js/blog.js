window.onload = function() {

  var content = document.getElementById("content").clientHeight;
  var bodyH = document.getElementsByTagName("body")[0].offsetHeight;
  var bigvwport = bodyH > content;
  var footer = document.getElementById("footer");
  var content = document.getElementById("content");

  footer_rect = footer.getBoundingClientRect();
  content_rect = content.getBoundingClientRect();

  no_overlap = footer_rect.top > content_rect.bottom || content_rect.bottom < footer_rect.top;

  if (!no_overlap) {
    footer.classList.remove("fixed-bottom");
    footer.style.position = "relative";
    footer.classList.add("mt-3");
  }

  window.addEventListener("resize", function(){
    var footer = document.getElementById("footer");
    var content = document.getElementById("content");
    var body = document.body.clientHeight;
    var sizeTest = content.clientHeight < body;
    var relfooter = footer.style.position == "relative";

    var footer_rect = footer.getBoundingClientRect();
    var content_rect = content.getBoundingClientRect();

    var no_overlap = footer_rect.top > content_rect.bottom || content_rect.bottom < footer_rect.top;


    if (!no_overlap) {
      footer.style.position = "relative";
      footer.classList.remove("fixed-bottom");
      footer.classList.add("mt-3");
    }
     if (relfooter && sizeTest) {
      footer.style.position = "fixed";
      footer.classList.add("fixed-bottom");
    }

  });
}
