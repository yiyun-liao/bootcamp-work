;
function renderCompany2(c) {
    c.id = 4385496;
    console.log(c.id, c.name, c.size);
    if (c.desc != undefined) {
        console.log(c.desc);
    }
}
;
var a = renderCompany2({
    id: 123445,
    name: "test",
    size: 225,
    desc: "nice",
});
renderCompany2({
    id: 195445,
    name: "test",
    size: 5,
});
