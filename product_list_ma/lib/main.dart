import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:badges/badges.dart' as badges;

import 'product_detail.dart';
import 'product_list.dart';

void main() {
  runApp(HomeScreen());
}

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Dashboard(),
    );
  }
}

class Dashboard extends StatelessWidget {
  const Dashboard({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Dashboard"),
          actions: [
            // Padding(
            //   padding: EdgeInsets.only(right: 20),
            //   child: IconButton(onPressed:(){}, icon: Icon(Icons.point_of_sale_outlined)),
            // ),
            Padding(
              padding: EdgeInsets.only(left: 0, right: 10, bottom: 10),
              child: badges.Badge(
                badgeContent: Text(
                  "10",
                  style: TextStyle(fontSize: 10, color: Colors.yellow),
                ),
                badgeStyle: badges.BadgeStyle(
                  badgeColor: Colors.blueAccent,
                  padding: EdgeInsets.all(5),
                  borderRadius: BorderRadius.circular(10),
                  borderSide: BorderSide(color: Colors.white, width: 1),
                  elevation: 10,
                ),
                onTap: () {
                },
                child: Icon(Icons.notifications),
              ),
            ),
          ],
        ),
        drawer: Drawer(
          child: Column(
            children: [
              const UserAccountsDrawerHeader(
                  accountName: Text(
                    "Kimhong",
                  ),
                  accountEmail: Text("yornkimhong@gmail.com"),
                  currentAccountPicture: CircleAvatar(
                    backgroundColor: Colors.white,
                    backgroundImage: NetworkImage(
                        "https://img.freepik.com/premium-vector/labubu-small-monster-illustration_873609-5290.jpg?w=360"),
                  )),
              ListTile(
                leading: const Icon(
                  Icons.line_style,
                  size: 50,
                ),
                title:
                const Text("Product List", style: TextStyle(fontSize: 18)),
                subtitle: const Text("display all product item..."),
                onTap: () {
                  Navigator.push(context,
                      MaterialPageRoute(builder: (context) => ProductList()));
                },
              ),

              const Expanded(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    Text(
                      "Version 1.0",
                      style: TextStyle(color: Colors.grey),
                    ),
                    SizedBox(
                      height: 10,
                    )
                  ],
                ),
              )
            ],
          ),
        ),
        body: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Column(
            children: [
             const  SizedBox(
                height: 10,
              ),
              Row(
                children: [

                  const SizedBox(
                    height: 10,
                  ),
                  Expanded(
                    child: InkWell(
                      child: const Card(
                        child: SizedBox(
                          height: 100,
                          child: Column(
                            children: [
                              Icon(
                                Icons.list_alt,
                                size: 70,
                                color: Colors.lightBlue,
                              ),
                              Text(
                                "Product List",
                                style: TextStyle(
                                  fontSize: 18,
                                  fontWeight: FontWeight.bold,
                                  color: Colors.grey,
                                ),
                              )
                            ],
                          ),
                        ),
                      ),
                      onTap: () {
                        Navigator.push(context, MaterialPageRoute(builder: (context) => ProductList()));
                      },
                    ),
                  )
                ],
              ),
              SizedBox(
                height: 10,
              ),
            ],
          ),
        ));
  }
}