function sendAmount() {
  toSendAmount = prompt(`Remaining Balance: {{user.additionalCreds.currentBalance}} \n\n Enter Advance Payment Amount`);
  csrftoken = `{{csrf_token}}`;
  remainingBalance = parseInt("{{user.additionalCreds.currentBalance}}");
  if (parseInt(toSendAmount) >= 1) {
    if (parseInt(remainingBalance) > toSendAmount) {
      alert("Sending Please Wait..");
    } else {
      return alert("Not enough Balance\n\n Remaining Balance: " + remainingBalance);
    }
  } else {
    alert("Not Valid amount");
    return;
  }
  fetch("/apis/makepayment/{{pageUser.userID}}/", {
    headers: { "X-CSRFToken": csrftoken, Accept: "application/json", "Content-Type": "application/json" },
    method: "POST",
    body: JSON.stringify({
      amount: toSendAmount,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      alert(data["message"]);
    });
}
