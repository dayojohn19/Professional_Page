// <div class="bg-body-tertiary p-5 rounded">
// <h1>Lets Chat</h1>
// <form id="Chat_Message_Form">
//   <div class="col-md-6">
//     <div class="input-group">
//       <input type="text" name="message" class="form-control" placeholder="Message" aria-label="Input group example" aria-describedby="basic-addon1" required />
//       <button type="submit" class="btn btn-primary" id="Chat_Message_Send_Button" style="margin: 0 auto">
//         <svg width="16" height="16" fill="currentColor" class="bi bi-chat" viewBox="0 0 16 16">
//           <path d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894zm-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z"></path>
//         </svg>
//         Send
//       </button>
//     </div>
//   </div>
// </form>
// <div id="Chat_Message_Container"></div>
// </div>

// let url = `ws://${window.location.host}/ws/socket-server/`;
// INFORMATION
// ------------------------
// README
// ------------------------
API_URL_CHAT = "127.0.0.1:8000";
// ------------------------
// ------------------------
// ------------------------
// ------------------------
// ------------------------
document.querySelector("#JoinPublicChat").addEventListener("click", () => {
  console.log("Joining Public Chat");
});
function JoinPublicChat() {
  console.log("Joining Public Chat");

  // let url = `ws://${API_URL_CHAT}/ws/socket-server/`;
  // room_name = JSON.parse({ room_name: "second_room_name" });
  // let url = `ws://${API_URL_CHAT}/${room_name}/ws/socket-server/`;
  // TODO CHANGE ROOM_NAME to real room
  let room_name = "Sole";
  let url = `ws://${API_URL_CHAT}/ws/${room_name}/socket-server/`;
  const chatSocket = new WebSocket(url);

  chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);
    console.log("Data: ", data);
    console.log("Data: ", data.type);

    // if (data.type === "chat") {
    if (data.type === "chat_message") {
      data.message = check_if_in_message(data.message);
      let messages = document.getElementById("Chat_Message_Container");
      // messages.insertAdjacentHTML("beforeend",`<div><p>${data.message}</p></div>`);
      default_name_message = "default_name_message";
      chat_item_container = `
    
    <a href="#" class="list-group-item list-group-item-action d-flex gap-3 py-3" aria-current="true">
      <img src="https://github.com/twbs.png" alt="twbs" width="32" height="32" class="rounded-circle flex-shrink-0" />
      <div class="d-flex gap-2 w-100 justify-content-between">
        <div>
          <h6 class="mb-0">${default_name_message}</h6>
          <p class="mb-0 opacity-75">${data.message}</p>
        </div>
        <small class="opacity-50 text-nowrap">now</small>
      </div>
    </a>    
    `;
      // messages.insertAdjacentHTML("afterend", `<div><p>${data.message}</p></div>`);
      messages.insertAdjacentHTML("afterend", chat_item_container);
    }
  };
}
let form = document.getElementById("Chat_Message_Form");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  let message = e.target.message.value;
  chatSocket.send(
    JSON.stringify({
      message: message,
    })
  );
  form.reset();
});
function check_if_in_message(console_message) {
  if (console_message.indexOf("connect") <= 0) {
    // console.log(console_message.indexOf("connect") <= 0);
    // GET USER LOCATION and IP ADDRESS
    console.log("Create something if new User Joined /static/js/chat.js");
    return console_message;
  } // 7
  else {
    console.log("Old User");
    return console_message;
  }
}
