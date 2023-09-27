function text(url) {
  return fetch(url).then((res) => res.text());
}

text("https://www.cloudflare.com/cdn-cgi/trace").then((data) => {
  let ipRegex = /[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}/;
  let ip = data.match(ipRegex)[0];
  console.log(ip);
});
