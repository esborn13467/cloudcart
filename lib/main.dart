import 'package:flutter/material.dart';

void main() {
  runApp(CloudCartApp());
}

class CloudCartApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Cloud Cart',
      theme: ThemeData(
        primarySwatch: Colors.purple,
      ),
      home: HomeScreen(),
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        elevation: 0,
        title: Row(
          children: [
            Container(
              decoration: BoxDecoration(
                color: Colors.purple.shade50,
                borderRadius: BorderRadius.circular(20),
                border: Border.all(color: Colors.purple, width: 2),
              ),
              padding: EdgeInsets.symmetric(horizontal: 12, vertical: 8),
              child: Row(
                children: [
                  Icon(Icons.cloud, color: Colors.purple),
                  SizedBox(width: 5),
                  Text(
                    'Cloud Cart',
                    style: TextStyle(
                      fontSize: 20,
                      fontWeight: FontWeight.bold,
                      color: Colors.purple,
                    ),
                  ),
                ],
              ),
            ),
            Expanded(
              child: SingleChildScrollView(
                scrollDirection: Axis.horizontal,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    CategoryButton(
                      label: 'Phone Accessories',
                      onTap: () => Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => PhoneAccessoriesScreen()),
                      ),
                    ),
                    CategoryButton(
                      label: 'Audio',
                      onTap: () => Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => AudioScreen()),
                      ),
                    ),
                    CategoryButton(
                      label: 'Power',
                      onTap: () => Navigator.push(
                        context,
                        MaterialPageRoute(builder: (context) => PowerScreen()),
                      ),
                    ),
                    CategoryButton(
                      label: 'Watches',
                      onTap: () => Navigator.push(
                        context,
                        MaterialPageRoute(
                            builder: (context) => WatchesScreen()),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
        actions: [
          IconButton(
            icon: Icon(Icons.search, color: Colors.purple),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => SearchScreen()),
              );
            },
          ),
          IconButton(
            icon: Icon(Icons.shopping_cart, color: Colors.purple),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => CartScreen()),
              );
            },
          ),
          IconButton(
            icon: Icon(Icons.person, color: Colors.purple),
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => ProfileScreen()),
              );
            },
          ),
        ],
      ),
      body: Column(
        children: [
          Container(
            height: 200,
            margin: EdgeInsets.symmetric(vertical: 10),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(15),
              color: Colors.purple.shade50,
            ),
            child: Center(
              child: Text(
                'Adverts Slideshow Here',
                style: TextStyle(color: Colors.purple),
              ),
            ),
          ),
          Expanded(
            child: Padding(
              padding: const EdgeInsets.symmetric(horizontal: 8.0),
              child: GridView.builder(
                gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                  crossAxisCount: 2,
                  crossAxisSpacing: 10,
                  mainAxisSpacing: 10,
                ),
                itemCount: 10,
                itemBuilder: (context, index) {
                  return ProductCard(productName: 'Product $index');
                },
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class CategoryButton extends StatelessWidget {
  final String label;
  final VoidCallback onTap;

  const CategoryButton({required this.label, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 5.0),
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          backgroundColor: Colors.white,
          foregroundColor: Colors.purple,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(20),
          ),
        ),
        onPressed: onTap,
        child: Text(label, style: TextStyle(fontSize: 12)),
      ),
    );
  }
}

class ProductCard extends StatelessWidget {
  final String productName;

  const ProductCard({required this.productName});

  @override
  Widget build(BuildContext context) {
    return Card(
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10),
      ),
      elevation: 4,
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(Icons.shopping_bag, size: 50, color: Colors.purple),
          SizedBox(height: 10),
          Text(productName, style: TextStyle(fontWeight: FontWeight.bold)),
        ],
      ),
    );
  }
}

// Search Screen
class SearchScreen extends StatefulWidget {
  @override
  _SearchScreenState createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> {
  final TextEditingController _searchController = TextEditingController();
  final List<String> _allProducts =
      List.generate(20, (index) => 'Product $index');
  List<String> _filteredProducts = [];

  @override
  void initState() {
    super.initState();
    _filteredProducts = _allProducts;
  }

  void _filterProducts(String query) {
    setState(() {
      _filteredProducts = _allProducts
          .where(
              (product) => product.toLowerCase().contains(query.toLowerCase()))
          .toList();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Search Products'),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextField(
              controller: _searchController,
              decoration: InputDecoration(
                hintText: 'Search for products...',
                border: OutlineInputBorder(),
                prefixIcon: Icon(Icons.search),
              ),
              onChanged: _filterProducts,
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: _filteredProducts.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(_filteredProducts[index]),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}

// Other Screens (Cart, Profile, and Categories)
class CartScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Your Cart')),
      body: Center(child: Text('Cart Page - Items in Cart')),
    );
  }
}

class ProfileScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Profile')),
      body: Center(child: Text('Profile Page - User Information')),
    );
  }
}

class PhoneAccessoriesScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Phone Accessories')),
      body: Center(child: Text('Phone Accessories Page')),
    );
  }
}

class AudioScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Audio')),
      body: Center(child: Text('Audio Page')),
    );
  }
}

class PowerScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Power')),
      body: Center(child: Text('Power Page')),
    );
  }
}

class WatchesScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Watches')),
      body: Center(child: Text('Watches Page')),
    );
  }
}
