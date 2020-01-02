# this is print tutorial

print("Let's practice everything.")
print("you\ 'd need to know that \'about escape with \\ that do:")
print("\n newlines and \t tabs.")

poem="""
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of lovely
nor comprehend passion from intuitions
and requires an explanation
\n\t\twhere and explanation
\n\twhere there is none
"""

print("----------------")
print(poem)
print("----------------")

five=10-2+3-6
print(f"this should be five:{five}")

def secret_formula(started):
    jelly_beans=started*500
    jars=jelly_beans /1000
    crates=jars/100
    return (jelly_beans , jars,crates)
start_point=10000
beans,jars,crates=secret_formula(start_point)


print("with a starting point of:{}".format(start_point))
print(f"we'd have {beans} beans ,{jars} jars , and {crates} crates")

start_point=start_point /10
print("we also can do in this way:")
formula=secret_formula(start_point)

print("we now have {} beans , {} jars,{}crates".format(beans,jars ,crates))
