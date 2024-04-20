//add front
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  addFront(value) {
    let newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    return this.head;
  }
}

//remote front
class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  class LinkedList {
    constructor() {
      this.head = null;
    }
  
    removeFront() {
      let removedNode = this.head;
      this.head = this.head.next;
      removedNode.next = null;
      return this 
    }
  }
      
//front value
class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  
  class LinkedList {
    constructor() {
      this.head = null;
    }
  
    getValue() {  
      return this.head.value;
    }
  }