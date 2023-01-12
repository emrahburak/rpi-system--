const https = require("https");
var express = require("express");
const TelegramBot = require("node-telegram-bot-api");
const fs = require("fs");
const bodyParser = require("body-parser");

require('dotenv').config();
const app = express();


const token = "5823147371:AAH40_n8WlNL8w51Jtqogh8sWQGKcepZXCg";

const url = "https://6eab-88-242-66-250.eu.ngrok.io"

// set telegram bot
const options = {
  webHook: {
    port:443
  }
};

const bot = new TelegramBot(token,options)
bot.setWebHook(url,{
  certificate:fs.readFileSync("./CA.pem","utf-8")
})


// set route, this route will be how to get requests

const rthw = `/bot${token}`;

app.post(rthw,(req,res) => {
  bot.processUpdate(req.body);
  console.log(req.body);
  res.sendStatus(200);
})


// Configuring express to use body-parser
// as middle-ware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('/', (req, res, next) => {
    res.status(200).send('Hello world!');
  });


// Matches "/echo [whatever]"
bot.onText(/\/echo (.+)/, (msg, match) => {
  // 'msg' is the received Message from Telegram
  // 'match' is the result of executing the regexp above on the text content
  // of the message

  const chatId = msg.chat.id;
  const resp = match[1]; // the captured "whatever"

  // send back the matched "whatever" to the chat
  bot.sendMessage(chatId, resp);
});

// Listen for any kind of message. There are different kinds of
// messages.
bot.on("message", (msg) => {
  const chatId = msg.chat.id;

  var Hi = "hi";
  if (msg.text.toString().toLowerCase().indexOf(Hi) === 0) {
    bot.sendMessage(chatId, "Hello dear user");
  }
  var bye = "bye";
  if (msg.text.toString().toLowerCase().includes(bye)) {
    bot.sendMessage(msg.chat.id, "Hope to see you around again , Bye. " + msg.from.first_name);
  }

  // send a message to the chat acknowledging receipt of their message
  bot.sendMessage(chatId, "Received your message");
});



var https_options = {
  key: fs.readFileSync("./localhost.decrypted.key"),
  cert: fs.readFileSync("./localhost.crt"),
};

const server = https
  .createServer(https_options, app)
  .listen(3000, (req, res) => {
    console.log("Https server listening on %s:%s", "https://localhost", "3000");
  });
