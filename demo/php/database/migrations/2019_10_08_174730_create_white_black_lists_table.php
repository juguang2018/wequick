<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateWhiteBlackListsTable extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('white_black_lists', function (Blueprint $table) {
            $table->increments('id');
            $table->string('cwxid',255)->nullable(false)->comment('所属人wxid');
            $table->string('wxid',255)->nullable(false)->comment('被加入到黑白名单中的人');
            $table->tinyInteger('type')->default(0)->comment('用来区分是白名单还是黑名单 0(默认不在黑白名单中) 1白名单 2黑名单');
            $table->string('chatroom',255)->nullable()->comment('所在群id');
            $table->string('nick',255)->nullable()->comment('昵称');
            $table->string('headPic',255)->nullable()->comment('头像');
            $table->text('auth')->nullable()->comment('权限字段 保留字段 里面保存的是json字符串');
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('white_black_lists');
    }
}
