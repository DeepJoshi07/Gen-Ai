masala_spices = ("cardamom","cloves","cinnamom")
(s1,s2,s3) = masala_spices
print(f"main masala spices: {s1}, {s2}, {s3}.")

ratio1,ratio2 = 2,1
print(f"Ratio is G :{ratio1} and C: {ratio2}")
ratio1,ratio2 = ratio2,ratio1
print(f"Ratio is G :{ratio1} and C: {ratio2}")

masala_spices2 = (["cardamom"],"cloves","cinnamom")
masala_spices2[0].append("anything")
print(masala_spices2)

# membership

print(f"is ginger in masala spices ? {"ginger" in masala_spices}")
print(f"is cinnamom in masala spices ? {"cinnamom" in masala_spices}")