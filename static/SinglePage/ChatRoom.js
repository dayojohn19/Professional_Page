function Chat_Roomm(room_name = null, user_username = null) {
  if (room_name == null) {
    this.room_name = prompt("Room Name: ").split(/\W+/).join("_");
  } else {
    this.room_name = room_name.split(/\W+/).join("_");
  }
  console.log(this.user_username);
  do {
    this.user_username = prompt("Your Nickname: ").split(/\W+/).join(" ");
    // input_user_username = prompt("Your Nickname: ");
    // console.log("\nTHIS: ", input_user_username);
    // this.user_username = "input_user_username";
    // console.log(this.user_username);
  } while (this.user_username == null);

  // else {
  // this.user_username = user_username;
  // }

  // this.base_url = "127.0.0.1:8000";
  this.base_url = "professional-website-2a09915461ba.herokuapp.com";
  //   this.user_username = "KOKO MELON";
  // Creating Socket
  this.socket_url = `ws://${this.base_url}/ws/${this.room_name}/socket-server/`;
  this.chatSocket = new WebSocket(this.socket_url);

  //   Creating Room Container
  this.room_container = document.createElement("div");
  this.room_container.setAttribute("class", "bg-body-tertiary p-5 rounded single-chat-room");
  this.Form_Object = document.createElement("form");
  this.Form_Object.setAttribute("id", `Chat_Message_Form_${this.room_name}`);
  this.Form_Object.setAttribute("class", `form_message_input_box`);
  this.Form_Object.innerHTML = `
  <div class="col-md-6">
    <div class="input-group">
      <input id="Chat_Message_Input_${this.room_name}" type="text" name="message" class="form-control" placeholder="Message" aria-label="Input group example" aria-describedby="basic-addon1" required />
      <button type="submit" class="btn btn-primary" id="Chat_Message_Send_Button" style="margin: 0 auto">
        <svg width="16" height="16" fill="currentColor" class="bi bi-chat" viewBox="0 0 16 16">
          <path d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894zm-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z"></path>
        </svg>
        Send
      </button>
    </div>
  </div>
  `;
  this.Form_Object.insertAdjacentHTML("beforeend", `<h1>${this.room_name.split("_").join(" ")}</h1>`);
  this.Form_Object.addEventListener("submit", (e) => {
    e.preventDefault();
    let message = e.target.message.value;
    this.chatSocket.send(
      JSON.stringify({
        message: [message, this.user_username],
        username: `${this.user_username}`,
      })
    );
    this.Form_Object.reset();
  });

  this.room_container.appendChild(this.Form_Object);

  this.room_message_container = document.createElement("div");
  this.room_message_container.setAttribute("id", `Chat_Message_Container_${this.room_name}`);
  this.room_container.appendChild(this.room_message_container);
  //     `<div class="bg-body-tertiary p-5 rounded">
  //       <h1>Room Name ${this.room_name}</h1>
  //     <div id="Chat_Message_Container_${this.room_name}"></div>
  //   </div>`;

  this.AppendNewChatContainer = () => {
    console.log("Appending");
    // Querying the Page to Append
    ChatRoomContainer = document.getElementById("main-container-page-3");
    ChatRoomContainer.appendChild(this.room_container);

    console.log("Done Appending..");
  };
  this.AppendNewChatContainer();
  //   this.chat_messages_container = document.getElementById(`Chat_Message_Container_${this.room_name}`);
  //   this.chat_messages_container = this.room_container;

  this.chatSocket.onmessage = (e) => {
    data = JSON.parse(e.data);

    console.log("Data: ", data);
    console.log("Data: ", data.type);
    this.item_message_container = `
          <a href="#" class="list-group-item list-group-item-action d-flex gap-3 py-3" aria-current="true">
            <img src="https://github.com/twbs.png" alt="twbs" width="32" height="32" class="rounded-circle flex-shrink-0" />
            <div class="d-flex gap-2 w-100 justify-content-between">
              <div>
                <h6 class="mb-0">${data.username}:</h6>
                <p class="mb-0 opacity-75">${data.message.split("_").join(" ")}</p>
              </div>
              <small class="opacity-50 text-nowrap">now</small>
            </div>
          </a>
          `;
    if (data.type === "chat") {
      //   this.chat_messages_container.insertAdjacentHTML("afterend", this.item_message_container);
      this.room_message_container.insertAdjacentHTML("afterend", this.item_message_container);
      console.log("Container: ", this.room_message_container, "\n\n");
      //   this.room_message_container.innerHTML = "<h1>hihi</h1>";
    }
  };

  //   this.SendMessage = function (YourMessage) {
  //     this.chatSocket.send(
  //       JSON.stringify({
  //         message: `${this.user_username}: ${YourMessage}`,
  //       })
  //     );
  //   };

  return this;
}

//
//
//
//
//
//
//
// BACKUP
function Chat_RoommBACKUP(room_name) {
  this.room_name = room_name;
  //   Creating Room Container
  this.this.room_container = document.createElement("div");
  this.room_container.setAttribute("class", "bg-body-tertiary p-5 rounded");
  this.room_container.innerHTML = `  <h1>Room Name ${this.room_name}</h1>
      <div id="Chat_Message_Container_${this.room_name}"></div>`;
  this.Form_Object = document.createElement("form");
  this.Form_Object.setAttribute("id", `Chat_Message_Form_${this.room_name}`);
  this.Form_Object.innerHTML = `
    <div class="col-md-6">
      <div class="input-group">
        <input id="Chat_Message_Input_${this.room_name}" type="text" name="message" class="form-control" placeholder="Message" aria-label="Input group example" aria-describedby="basic-addon1" required />
        <button type="submit" class="btn btn-primary" id="Chat_Message_Send_Button" style="margin: 0 auto">
          <svg width="16" height="16" fill="currentColor" class="bi bi-chat" viewBox="0 0 16 16">
            <path d="M2.678 11.894a1 1 0 0 1 .287.801 10.97 10.97 0 0 1-.398 2c1.395-.323 2.247-.697 2.634-.893a1 1 0 0 1 .71-.074A8.06 8.06 0 0 0 8 14c3.996 0 7-2.807 7-6 0-3.192-3.004-6-7-6S1 4.808 1 8c0 1.468.617 2.83 1.678 3.894zm-.493 3.905a21.682 21.682 0 0 1-.713.129c-.2.032-.352-.176-.273-.362a9.68 9.68 0 0 0 .244-.637l.003-.01c.248-.72.45-1.548.524-2.319C.743 11.37 0 9.76 0 8c0-3.866 3.582-7 8-7s8 3.134 8 7-3.582 7-8 7a9.06 9.06 0 0 1-2.347-.306c-.52.263-1.639.742-3.468 1.105z"></path>
          </svg>
          Send
        </button>
      </div>
    </div>
    `;
  this.Form_Object.addEventListener("submit", (e) => {
    e.preventDefault();
    let message = e.target.message.value;
    chatSocket.send(
      JSON.stringify({
        message: message,
      })
    );
    form.reset();
  });
  this.room_container.appendChild(this.Form_Object);
  //     `<div class="bg-body-tertiary p-5 rounded">
  //       <h1>Room Name ${this.room_name}</h1>
  //     <div id="Chat_Message_Container_${this.room_name}"></div>
  //   </div>`;

  this.AppendNewChatContainer = () => {
    console.log("Appending");
    ChatRoomContainer = document.getElementById("main-container-page-3");
    // this.room_container.insertAdjacentHTML("beforeend", this.room_form);
    // this.room_container.append(this.room_form);
    // ChatRoomContainer.insertAdjacentHTML("beforeend", this.room_container);
    ChatRoomContainer.appendChild(this.room_container);

    console.log("Done Appending..");
  };

  this.AppendNewChatContainer();
}
