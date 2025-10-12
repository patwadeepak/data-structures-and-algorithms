# https://leetcode.com/contest/biweekly-contest-167/problems/design-exam-scores-tracker/description/
import bisect

class ExamTracker:

    def __init__(self):
        self.ps = {}

    def record(self, time: int, score: int) -> None:
        if self.ps.keys():
            last_key = list(self.ps.keys())[-1]
            self.ps[time] = score + self.ps[last_key]
        else:
            self.ps[time] = score

    def totalScore(self, startTime: int, endTime: int) -> int:
        times = list(self.ps.keys())
        idx1 = bisect.bisect_left(times, startTime) - 1
        idx2 = bisect.bisect_left(times, endTime)
        if times[idx2] > endTime:
          idx2 -= 1

        if idx1 >= 0:
            return self.ps[times[idx2]] - self.ps[times[idx1]]
        elif idx2 >= 0:
            return self.ps[times[idx2]]
        else:
            return 0

if __name__=='__main__':
  et = ExamTracker()

  # et.record(1, 98)

  # print(et.totalScore(1, 1))

  # et.record(5, 99)
  # print(et.totalScore(1, 3))
  # print(et.totalScore(1, 5))
  # print(et.totalScore(3, 4))
  # print(et.totalScore(2, 5))

  et.record(2,2)
  print(et.totalScore(1,1))
  print(et.totalScore(1,2))
  print(et.totalScore(2,2))

"""
This python solution gives TLE on leetcode.
But same thing implmented in C++ is AC
""" 
