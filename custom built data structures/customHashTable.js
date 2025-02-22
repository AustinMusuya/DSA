class HashTable {
  constructor(size) {
    this.data = new Array(size);
  }

  _hash(key) {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = (hash + key.charCodeAt(i) * i) % this.data.length;
    }
    return hash;
  }

  set(key, value) {
    let address = this._hash(key);
    let item = [key, value];
    if (!this.data[address]) {
      this.data[address] = [];
    }
    this.data[address].push(item);

    return this.data;
  }

  get(key) {
    let address = this._hash(key);
    let currentBucket = this.data[address];
    if (currentBucket) {
      for (let i = 0; i < currentBucket.length; i++) {
        if (currentBucket[i][0] == key) {
          return currentBucket[i][1];
        }
      }
    }
    return undefined;
  }
}

const myHashTable = new HashTable(50);
myHashTable.set("grapes", 10000);
// myHashTable.get("grapes");
myHashTable.set("apples", 9);
myHashTable.get("apples");

console.log(myHashTable);
// expected output

// HashTable { data: [ <50 empty items> ["grapes", 10000],["apples", 5000],["mangoes", 55] ] }
