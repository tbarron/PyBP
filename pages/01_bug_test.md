---
title: 3. Find a Bug, Write a Test
---
You just found a bug in your code. What's the first thing you do?

I think most us of start looking at the code trying to figure out
where the problem is and what to do about it. I know that's my
instinctive first response.

I'd like to suggest that a better first step is to write a test that
demonstrates the presence of the bug by tickling it and failing. Then,
when we remove the bug, our new test will start working. And we'll
have a more complete, more robust test suite.

**Why**: Capturing knowledge about past bugs in tests allows us to
  code with confidence, knowing that any regressions will be exposed
  the next time we run our tests. (Well, *know* may be a little
  strong. But you get the idea. We build confidence in our code by seeing
  it pass the tests we've devised for it. The better and more complete the
  test suite is, the higher our confidence level will be.)

**How**: Write a new test case and make sure it fails with the current
  code, demonstrating the newly discovered bug. If you find more bugs in
  the process of constructing the new test, write a test for each one.

