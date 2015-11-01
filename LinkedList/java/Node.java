
public class Node {
	private int val;
	private Node next;
	
	public Node(int val, Node next){
		this.setVal(val);
		this.setNext(next);
	}

	public int getVal() {
		return val;
	}

	public void setVal(int val) {
		this.val = val;
	}

	public Node getNext() {
		return next;
	}

	public void setNext(Node next) {
		this.next = next;
	}	
}
