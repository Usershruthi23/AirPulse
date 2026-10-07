const $ = id => document.getElementById(id);
let history = Array.from({length:70}, (_,i)=>0.1*Math.sin(i/4));
let currentPose = "standing";

function draw(samples){
  const c=$("chart"), ctx=c.getContext("2d");
  const dpr=window.devicePixelRatio||1, w=c.clientWidth, h=c.clientHeight;
  c.width=w*dpr; c.height=h*dpr; ctx.setTransform(dpr,0,0,dpr,0,0);
  ctx.clearRect(0,0,w,h);
  ctx.strokeStyle="#19324a"; ctx.lineWidth=1;
  for(let y=20;y<h;y+=50){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(w,y);ctx.stroke();}
  const all=samples||[];
  ctx.strokeStyle="#35d6b1"; ctx.lineWidth=2; ctx.beginPath();
  all.forEach((v,i)=>{
    const x=i/(all.length-1)*w, y=h/2-v*h*.22;
    i?ctx.lineTo(x,y):ctx.moveTo(x,y);
  }); ctx.stroke();
}

async function refresh(){
  try{
    const r=await fetch("/api/vitals");
    const d=await r.json();
    $("heart").textContent=d.heartRate;
    $("resp").textContent=d.respirationRate;
    $("motion").textContent=d.motion;
    $("quality").textContent=d.signalQuality;
    $("poseName").textContent=d.poseLabel;
    $("poseDescription").textContent=d.description;
    $("sPose").textContent=d.poseLabel;
    $("sStatus").textContent=d.status;
    $("status").textContent=d.status;
    document.querySelectorAll(".pose-buttons button").forEach(b=>b.classList.toggle("active",b.dataset.pose===d.pose));
    draw(d.samples);
    const p=d.pose;
    $("person").style.transform =
      p==="sitting" ? "translateY(35px) rotate(2deg)" :
      p==="walking" ? "translateX(8px) rotate(-5deg)" :
      p==="running" ? "translateX(8px) rotate(-12deg) scale(1.04)" :
      p==="lying" ? "rotate(90deg) translateX(40px)" :
      p==="sleeping" ? "rotate(90deg) translateX(40px)" : "none";
  }catch(e){
    $("status").textContent="Backend offline";
  }
}

document.querySelectorAll(".pose-buttons button").forEach(btn=>{
  btn.addEventListener("click",async()=>{
    currentPose=btn.dataset.pose;
    await fetch("/api/pose/"+currentPose,{method:"POST"});
    refresh();
  });
});
window.addEventListener("resize",refresh);
refresh();
setInterval(refresh,1000);
