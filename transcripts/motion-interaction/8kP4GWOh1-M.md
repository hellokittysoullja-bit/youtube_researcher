# CAD integration with organic haptic design
Simon Brand · 4 мин · 699 просмотров · en · https://youtu.be/8kP4GWOh1-M



[00:01] this is a video of free form modeling plus version 10 demonstrating how to easily add sculptural detail that cannot be created in your typical CAD to a parametrically represented model it Bridges the gap between the organic limitations of Cad and free forms 3D sculpting so this is the free form modeling plus uh version 10 interface and what I'm going to do is import a previously created step file design that was created in Rhino um and then I'm going to import a previously created sculptural design that was done in free form as you can see we have a bare 

[00:33] sculpture design on top of a baby's bottle and what I want to do is I actually want to put this be design into the uh the solid model that is the baby's bottle um but since we have two different types of geometries um we need to stitch this into the model and since this type of model is not done in CAD uh we need to do it in free form and then Stitch it uh into this model afterwards so what I'm doing now is I'm creating a trim line for this model and I'm actually going to delete the inside of 

[01:05] this surface on the baby's bottle and thicken it with an overbuild to a voxal geometry and the reason why we've thickened it um with an overbuild is so that we have um a substantial amount of geometry with a with an overlap so that when we do create a surface we have some overlap to trim and then Stitch uh the surfaces into the model of the baby's bottle so what I'm doing right now is I'm using my tug tool to actually push 

[01:35] some of the overlapping geometry that we don't need um into the thickened part so that we don't have any excess uh data on the back side and once that is completed we can hit the apply button uh on the dino bar and that will apply those changes uh once we've done that we want to actually combine the thickened part into the design of the bear so that we have one piece and we can do that easily through the combined into booing technique on the object list um and 

[02:07] that's a very simple function in free form as opposed to doing Boolean and shelling and things like that in CAD can be very difficult and frustrating um because of the innate problems with those types of functions with surface and solid data but since we're working with a completely different geometry called voxal um those types of functions work very well uh in free form so right now I'm actually um using my smooth tool to paint the seams um of this design so that we can blend in the edges and give 

[02:38] it a nice rounded radius um this is kind of a uh replacement for a fillet tool in some cases um and it's used to get rid of unwanted data in this case it works really well for blending in uh the seam so what I'm going to do now is go back to my edit and Stitch solid tool and I'm going to use the original trim line curve Cur and I'm going to select the geometry of the voxal um and then hit Stitch and what this is going to do is it's going to bring up our Auto surfacer 

[03:09] module um which will allow us to take the voxal geometry which is representing the bear um import it as a mesh file and then we're going to surface this mesh file to nerve geometry so that we can stitch it back into the uh baby's bottle design and this is a very useful um application because free form is really the only tool that allows you to work with voxal geometry nerves geometry and mesh geometry and these are all um 

[03:40] useful geometries but they maintain shapes differently obviously you can see with the voxal geometry the bear is very sculptural something like that cannot be created in CAD um so doing it in free form and then being able to surface it and Stitch it into one closed piece uh is is inv valuable um so what I'm doing right now is I'm actually um surfacing this model in the auto surfacer and what I've done is I've selected a number of surfaces with a number of control points and those can all be changed to to get 

[04:12] uh the auto surfacer to surface the way you'd like um and then when I hit save what it's going to do is it's going to import this surface model now back into free form and it's going to automatically trim it based on the curv trim line that I created at the very beginning of this demo and now you can see I've taken that bare design and surfaced it and trimmed it and stitched it all back into this bottle so that we have one closed 

[04:43] solid 
