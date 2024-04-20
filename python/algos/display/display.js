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
  
    insertValue(value) {
      const newNode = new Node(value);
      newNode.next = this.head;
      this.head = newNode;
      return this.head;
    }
  
    display() {
      let runner = this.head;
      let result = '';
  
      while (runner) {
        result += runner.value + ' ';
        runner = runner.next;
      }
  
      return result
    }
  }