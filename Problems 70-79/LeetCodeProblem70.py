class Solution:#Calculate how many distinct ways you can reach the top of an n step staircase if you can climb either 1 or 2 steps each time
    def climbStairs(self, n: int) -> int:
        #turns out there is a less memory intensive solution, I'll put that here above the
        #old one

        #base case, we're going from n /down/ to 0 this time
        one, two = 1, 1 #dont need whole array, just save last two values.

        for i in range(n-1):
            #smartly recognize going from one (which is one step down) to 0 is n-1 steps
            temp = one #store one so that it can become new value of two
            one = one + two #variable now looks at value of 1 step down from where it was
            two = temp
        
        return one #and then that's it, you just return the value it reaches at the bottom.


	#Also, I included a slower attempt below just to show where my thought process was before finding a better path forward

        #first we make a dict that'll be our dp table and base cases inside
        #tab = {1: 1, 2: 2}
        #if n < 1:
        #    return 0

        #let's make a function to call
        #def calcTab(tab, i):
        #    if i in tab:
        #        return tab[i]
        #    else:
        #        ans = calcTab(tab, i-2) + calcTab(tab, i-1)
        #        tab.update({i: ans})
        #        return tab[i]
        
        #return calcTab(tab, n)
        
