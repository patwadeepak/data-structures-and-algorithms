// https://leetcode.com/contest/biweekly-contest-167/problems/design-exam-scores-tracker/description/
#include <bits/stdc++.h>
#define ll long long

using namespace std;

class ExamTracker {
public:
  map<long long, long long> ps;
  ExamTracker() {}

  void record(ll time, ll score) {
    if (ps.empty())
    {
      ps[time] = score;
    }
    else
    {
      ll lcs = ps.rbegin()->second;
      ps[time] = score + lcs;
    }
  }

  long long totalScore(ll startTime, ll endTime) {
    auto it_end = ps.upper_bound(endTime);
    if (it_end == ps.begin())
    {
      return 0;
    }

    it_end--;
    ll score_at_end = it_end->second;

    auto it_start = ps.lower_bound(startTime);

    if (it_start == ps.begin())
    {
      return score_at_end;
    }

    it_start--;
    ll score_at_subtract = it_start->second;

    return score_at_end - score_at_subtract;
  }
};
