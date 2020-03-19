
//This is Just the same method with ../Leetcode/ugly-number-ii.cpp
object DblLinear {

  def dblLinear(n: Int): Int = {
    var u = Vector(1)
    var i = 1
    var (p2, p3) = (0, 0)

    while(i <= n) {
      u = u :+ math.min(2 * u(p2) + 1, 3 * u(p3) + 1)
      if(u(i) == 2 * u(p2) + 1) p2 += 1
      if(u(i) == 3 * u(p3) + 1) p3 += 1
      i += 1
    }
    u(n)
  }
}




