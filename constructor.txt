'''
== Object Completeness

When the constructor finishes, the object should be complete and well-formed

**Why**: If two operations are not tied together by the code but I have to
remember to followup A with B, sooner or later I'm going to forget B. 

**How**: Just make sure that at the end of +{ul}init(){ul}+, all the
attributes of the object have been set to a valid value.

=== Example

**Poor**: 
----
import Human
p = Human.Person()                                    <1>
p.name = "George"
p.age = 75
p.married = True
----
 <1> The constructor has finished at this point, but the person has no
 name, age, or marital status.

**Better**:
----
import Human
p = Human.Person(name="George", age=75, married=True) <2>
----
 <2> When the constructor completes, all of the members of p are set. 

The example is adapted from
http://stevenloria.com/python-best-practice-patterns-by-vladimir-keleshev-notes[Python
Best Practices Patterns, Vladimir Keleshev]
footnoteref:[n1,http://stevenloria.com/python-best-practice-patterns-by-vladimir-keleshev-notes[Python Best Practice Patterns]]
