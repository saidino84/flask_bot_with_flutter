import 'dart:convert';

import 'package:bubble/bubble.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  // ignore: unused_field
  final _listkey = GlobalKey<AnimatedListState>();
  var _data = <String>[];

  //no Flask eu define arota de query /bot
  static const String BOT_URL =
      'https://flaskchatbotmoz.herokuapp.com/bot'; //na routa bot
  var queryController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[300],
      appBar: AppBar(
        title: Text('Chat-bot'),
        centerTitle: true,
      ),
      body: Stack(
        children: [
          AnimatedList(
            key: _listkey,
            initialItemCount: _data.length,
            itemBuilder: (ctx, int index, Animation<double> animation) {
              return _buildMessageItem(_data[index], animation, index);
            },
          ),
          Align(
            alignment: Alignment.bottomCenter,
            child: ColorFiltered(
              colorFilter: ColorFilter.linearToSrgbGamma(),
              child: Container(
                color: Colors.white,
                child: Padding(
                  padding: EdgeInsets.only(
                    left: 20,
                    right: 20,
                  ),
                  child: TextField(
                      maxLines: 4,
                      controller: queryController,
                      decoration: InputDecoration(
                        icon: Icon(
                          Icons.message,
                          color: Colors.blue,
                        ),
                        hintText: 'Write your message ...',
                        fillColor: Colors.redAccent,
                        suffixIcon: IconButton(
                          onPressed: () {
                            this.getResponse();
                            // queryController.text = 'send';
                          },
                          icon: Icon(
                            Icons.send,
                          ),
                        ),
                      ),
                      textInputAction: TextInputAction.send,
                      onSubmitted: (message) {
                        this.getResponse();
                        queryController.text = '';
                      }),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  void getResponse() {
    if (queryController.text.length > 0) {
      this.insertSingleItem(queryController.text);

      var cliente = this.getClient();

      try {
        cliente.post(
          Uri.parse(BOT_URL),
          body: {'query': queryController.text},
        )..then((resposta) {
            // Map<String, dynamic> dados = jsonDecode(resposta.body);
            print("===============>${resposta.body}");
            insertSingleItem(resposta.body + '<bot>');
          });
      } finally {}
    }
  }

  void insertSingleItem(String text) {
    _data.add(text);
    _listkey.currentState!.insertItem(_data.length - 1);
  }

  http.Client getClient() {
    return http.Client();
  }
}

Widget _buildMessageItem(
    String message, Animation<double> animacao, int index) {
  bool isMymsg = message.endsWith("<bot>");
  return SizeTransition(
    sizeFactor: animacao,
    child: Padding(
      padding: isMymsg
          ? EdgeInsets.only(top: 10, right: 120)
          : EdgeInsets.only(top: 10, left: 120),
      child: Container(
        // color: Colors.black12,

        alignment: isMymsg ? Alignment.topLeft : Alignment.topRight,
        child: Bubble(
          showNip: true,
          nip: isMymsg ? BubbleNip.leftTop : BubbleNip.rightTop,
          child: Text(message,
              style: TextStyle(
                color: isMymsg ? Colors.green : Colors.black,
              )),
          color: isMymsg ? Colors.black : Colors.green,
          padding: BubbleEdges.all(10),
        ),
      ),
    ),
  );
}
