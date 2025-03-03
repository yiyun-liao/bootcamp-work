//? and readonly=========================================================================
interface Company2{
    readonly id:number;
    name:string;
    size:number;
    desc?:string;
};

function renderCompany2(c:Company2):void{
    // c.id = 4385496;  //error
    console.log(c.id, c.name, c.size);
    if(c.desc != undefined){
        console.log(c.desc);
    }
};

let a = renderCompany2({
    id:123445,
    name:"test",
    size:225,
    desc:"nice",
});

renderCompany2({
    id:195445,
    name:"test",
    size:5,
});