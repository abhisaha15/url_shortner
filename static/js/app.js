//var columnDefs = [
//    {headerName: "RID", field: "rid",hide:true},
//    {headerName: "URL Short Name", field: "u_st_nm",checkboxSelection: true},
//    {headerName: "Actual URL", field: "a_url"},
//    {headerName: "Created Time", field: "creation_time"},
//  ];
//
//  // specify the data
//  var rowData ={{data}} ;
//  //call a seperate api to get data of user specific urls
//
//
//  // let the grid know which columns and what data to use
//  var gridOptions = {
//    defaultColDef: {
//        resizable: true,
//    },
//    suppressDragLeaveHidesColumns: true,
//    columnDefs: columnDefs,
//    onFirstDataRendered: onFirstDataRendered,
//
//    rowData: rowData
//  };
//  function onFirstDataRendered(params) {
//    params.api.sizeColumnsToFit();
//  }
//
//  // setup the grid after the page has finished loading
//  document.addEventListener('DOMContentLoaded', function() {
//      var gridDiv = document.querySelector('#myGrid');
//      new agGrid.Grid(gridDiv, gridOptions);
//  });
//
//
//
//
//function updatedata(){
//    console.log('save button in the update from is clicked')
//}
//
//function deletedata(){
//    console.log('delete button in the update from is clicked')
//}
//
//
//function adddata(){
//    console.log('add button in the add from is clicked')
//}
//
//
//
//  document.querySelector('#urlcontrol').addEventListener('click',function(){
//    var selectedRow = gridOptions.api.getSelectedRows();
//
//    if(selectedRow[0]){
//        document.querySelector('.modal-title').innerHTML=`Update URL Data`;
//        document.querySelector('.modal-body').innerHTML=`
//            <form class="row g-3">
//
//                <div class="col-12">
//                    <label for="inputURL" class="form-label">URL</label>
//                    <input type="text" class="form-control" id="inputURL" placeholder="https://www.google.com/">
//                </div>
//                <div class="col-12">
//                    <label for="inputURLName" class="form-label">Provide a Short Name</label>
//                    <input type="text" class="form-control" id="inputURLName" placeholder="favsite">
//                </div>
//
//                <div class="modal-footer">
//                    <button type="submit" class="btn btn-primary" onclick="updatedata()">Save</button>
//                    <button type="submit" class="btn btn-danger" onclick="deletedata()">Delete</button>
//                </div>
//            </form>`;
//
//    }else{
//
//        document.querySelector('.modal-title').innerHTML=`Add URL Data`;
//
//        document.querySelector('.modal-body').innerHTML=`
//            <form class="row g-3">
//
//                <div class="col-12">
//                    <label for="inputURL" class="form-label">URL</label>
//                    <input type="text" class="form-control" id="inputURL" placeholder="https://www.google.com/">
//                </div>
//                <div class="col-12">
//                    <label for="inputURLName" class="form-label">Provide a Short Name</label>
//                    <input type="text" class="form-control" id="inputURLName" placeholder="favsite">
//                </div>
//
//                <div class="modal-footer">
//                    <button type="submit" class="btn btn-primary" onclick="adddata()">Save</button>
//                </div>
//            </form>`;
//
//    }
//
//  })
