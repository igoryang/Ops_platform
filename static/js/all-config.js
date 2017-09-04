//override dialog's title function to allow for HTML titles
$.widget("ui.dialog", $.extend({}, $.ui.dialog.prototype, {
    _title: function(title) {
        var $title = this.options.title || '&nbsp;'
        if( ("title_html" in this.options) && this.options.title_html == true )
            title.html($title);
        else title.text($title);
    }
}));

var DATATABLE_CONFIG = {
    "sDom": "t<'row'<'col-sm-6'i><'col-sm-6'p>>",
    "bFilter" : false,
    "bSort": false,
    "aLengthMenu": [25, 50, 100],
    "iDisplayLength": 25,
    "bProcessing" : false, //DataTables载入数据时，是否显示‘进度’提示
    "bServerSide" : true, //是否启动服务器端数据导入
    "sServerMethod": "POST",   //以post的方式提交数据
    "bAutoWidth": false,
    "oLanguage": { //国际化配置
        "sProcessing": "正在获取数据，请稍后...",
        "sLengthMenu": "显示 _MENU_ 条",
        "sZeroRecords": "没有您要搜索的内容",
        "sInfo": "从 _START_ 到  _END_ 条记录 总记录数为 _TOTAL_ 条",
        "sInfoEmpty": "记录数为0",
        "sInfoFiltered": "(全部记录数 _MAX_ 条)",
        "sInfoPostFix": "",
        "sSearch": "搜索",
        "sUrl": "",
        "oPaginate": {
            "sFirst": "第一页",
            "sPrevious": "上一页",
            "sNext": "下一页",
            "sLast": "最后一页"
        }
    }
};

var showDialog = function(title, text, iconClass, title_id, text_id){
    title=title||'提示';
    text=text||'默认提示';
    iconClass=iconClass||'icon-warning-sign red';
    title_id=title_id||'dialog-alert';
    text_id=text_id||'dialog-text';

    $("#" + text_id)[0].textContent = text;
    $("#" + title_id).removeClass('hide').dialog({
        resizable: false,
        modal: true,
        title: "<div class='widget-header'><h4 class='smaller'><i class='" + iconClass + "'></i>" + title + "</h4></div>",
        title_html: true,
        buttons: [
            {
                html: "<i class='icon-remove bigger-110'></i>&nbsp;关闭",
                "class" : "btn btn-danger btn-xs",
                click: function() {
                    $( this ).dialog( "close" );
                }
            }
        ]
    });
};