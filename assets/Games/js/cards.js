var cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];
var suits = ["diamonds", "hearts", "spades", "clubs"];
var deck = new Array();

function getDeck() {
  var deck = new Array();

  for (var i = 0; i < suits.length; i++) {
    for (var x = 0; x < cards.length; x++) {
      var card = { Value: cards[x], Suit: suits[i] };
      deck.push(card);
    }
  }

  return deck;
}

function shuffle() {
  // for 1000 turns
  // switch the values of two random cards
  for (var i = 0; i < 1000; i++) {
    var location1 = Math.floor(Math.random() * deck.length);
    var location2 = Math.floor(Math.random() * deck.length);
    var tmp = deck[location1];

    deck[location1] = deck[location2];
    deck[location2] = tmp;
  }

  renderDeck();
}

function renderDeck() {
  document.getElementById("deck").innerHTML = "";
  for (var i = 0; i < deck.length; i++) {
    var card = document.createElement("div");
    var value = document.createElement("div");
    var suit = document.createElement("div");
    card.className = "card";
    value.className = "value";
    suit.className = "suit " + deck[i].Suit;

    value.innerHTML = deck[i].Value;
    card.appendChild(value);
    card.appendChild(suit);

    document.getElementById("deck").appendChild(card);
  }

  // import player
  var players = new Array();
  function createPlayers(num) {
    players = new Array();
    for (var i = 1; i <= num; i++) {
      var hand = new Array();
      var player = { Name: "Player " + i, ID: i, Points: 0, Hand: hand };
      players.push(player);
    }
  }

  function createPlayersUI() {
    document.getElementById("players").innerHTML = "";
    for (var i = 0; i < players.length; i++) {
      var div_player = document.createElement("div");
      var div_playerid = document.createElement("div");
      var div_hand = document.createElement("div");
      var div_points = document.createElement("div");

      div_points.className = "points";
      div_points.id = "points_" + i;
      div_player.id = "player_" + i;
      div_player.className = "player";
      div_hand.id = "hand_" + i;

      div_playerid.innerHTML = players[i].ID;
      div_player.appendChild(div_playerid);
      div_player.appendChild(div_hand);
      div_player.appendChild(div_points);
      document.getElementById("players").appendChild(div_player);
    }
  }
}

function load() {
  deck = getDeck();
  shuffle();
  renderDeck();
}

window.onload = load;
