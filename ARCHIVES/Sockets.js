function WebSocket_Object() {
  console.log("\n Creating Socket..\n");
  this.user_username = prompt("You Nickname: ");
  this.base_url = "127.0.0.1:8000";
  this.room_name = prompt("Room: ");
  this.socket_url = `ws://${this.base_url}/ws/${this.room_name}/socket-server/`;
  this.chatSocket = new WebSocket(this.socket_url);

  this.chatSocket.onmessage = function (e) {
    data = JSON.parse(e.data);
    console.log("Data: ", data);
  };

  this.form = document.getElementById("Chat_Message_Form");
  this.form.addEventListener("submit", (e) => {
    e.preventDefault();
    message = e.target.message.value;
    this.form.reset();
  });
  this.SendMessage = function (YourMessage) {
    this.chatSocket.send(
      JSON.stringify({
        message: `${this.user_username}: ${YourMessage}`,
      })
    );
  };
  return this;
}


