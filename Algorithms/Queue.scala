package test.algo.mutable


import scala.reflect.ClassTag

trait Queue[A] {
  def enqueue(x: A): Unit
  def dequeue(): Option[A]
  def isEmpty: Boolean
  def size: Int
}

trait Equal[A] {
  def ===(that: A): Boolean
  def =/=(that: A): Boolean = !(this === that)
}

trait Order[A] extends Equal[A] {
  def <(that: A): Boolean
  def >(that: A): Boolean = !(this < that) && !(this === that)
  def <=(that: A): Boolean = !(this > that)
  def >=(that: A): Boolean = !(this < that)
}


class ListQueue[A](seq: Seq[A]) extends Queue[A] {

  private var queue: List[A] = seq.toList
  def this() {
    this(Nil)
  }

  def size: Int = this.queue.length
  def isEmpty = this.queue.isEmpty
  def enqueue(x: A) {
    this.queue = x :: this.queue
  }
  def dequeue(): Option[A] = this.queue.lastOption
}


//class ListPriorityQueue[A <% Order[A]](seq: Seq[A]) extends Queue[A]


class ArrayPriorityQueue[A <% Ordered[A] : ClassTag](seq: Seq[A]) extends Queue[A] {

  val queue: Array[A] = seq.toArray
  val maxI: Int = seq.length - 1
  var I: Int = seq.length - 1
  def this(s: Int) {
    this(new Array[A](s + 1))
    this.I = 0
  }

  def size = this.I
  def isEmpty = this.I == 0
  def isFull = this.I == this.maxI
  private def inRange(i: Int): Boolean = i > 0 && i <= this.I
  private def notInRangeMsg() {
    println("Warning: Array Priority queue index not in range")
  }
  private def exch(i: Int, j: Int) {
    if(!inRange(i) || !inRange(j)) {
      notInRangeMsg()
      return
    }
    val tmp = this.queue(i)
    this.queue(i) = this.queue(j)
    this.queue(j) = tmp
  }
  private def swim(i: Int) {
    if(!inRange(i)) {
      notInRangeMsg()
      return
    }
    var j = i
    while(j > 1 && this.queue(j) > this.queue((j/2).toInt)) {
      exch(j, (j/2).toInt)
      j = (j/2).toInt
    }
  }
  private def sink(i: Int) {
    if(!inRange(i)) {
      notInRangeMsg()
      return
    }
    var j = i
    var ix = 0
    while(ix != -1 && j*2 < this.I) {
      ix = -1
      if(this.queue(j) < this.queue(j*2)) ix = j*2
      if(j*2 < this.I - 1 && this.queue(j) < this.queue(j*2+1)) {
        if(ix == -1) ix = j*2 + 1
        else if(this.queue(j*2) < this.queue(j*2+1)) ix = j*2 + 1
      }
      if(ix != -1) exch(j, ix)
      j = ix
    }
  }

  def enqueue(x: A) {
    if(this.isFull) {
      println("Warning: Priority queue is full, because of Array...")
      return
    }
    this.queue(this.I + 1) = x
    this.I = this.I + 1
    swim(this.I)
  }
  def dequeue(): Option[A] = {
    if(this.isEmpty) return None
    val x = this.queue(1)
    exch(1, this.I)
    sink(1)
    this.I = this.I - 1
    Some(x)
  }
}














