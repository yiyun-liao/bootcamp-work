const mysql=require("mysql2/promise");

async function connectToMySQL(){
    // 建立連線
    const con = await mysql.createConnection({
        user:"root",
        password:"12345678",
        host:"localhost",
        database:"practice"
    }); 
    console.log('連線成功')

    // INSERT INTO
    // let [results] =  await con.execute("INSERT INTO product(name) VALUES ('綠茶')")
    // console.log(results)
    
    // DELETE
    // let [results] =  await con.execute("DELETE FROM product WHERE id=8")
    // console.log(results)  
    
    // 將變數資料代入到 SQL 指令裡面
    // UPDATE
    // let newName='美式';
    // let productID=1;
    // let [results] =  await con.execute("UPDATE product SET name=? WHERE id=?", [newName,productID]);
    // console.log(results) 
    
    // 取得資料
    let [results] = await con.execute("SELECT * FROM product");
    // console.log(results);

    // 找到特定資料，1,直接印出 array 值。2, 直接在 SQL 查詢時用 WHERE id = 1。3, JS 搜尋
    // console.log(results[0]);
    for (let i=0; i<results.length; i++){
        let product=results[i];
        if (product.id === 1){
            console.log(product.name);
            break;
        }
    }
    // // 資料個別印出 forEach()
    // results.forEach((product)=>{
    //     console.log(product.name)
    // })
    // //資料個別印出 forEach()
    // for (let i=0; i<results.length; i++){
    //     let product=results[i];
    //     console.log(product.name)
    // }


    // 關閉連線
    con.end()  
}

connectToMySQL();